"""Build a documentary Graphify graph locally, without model calls or private files.

Run with a Python environment that already contains graphifyy. This is a
documentation tool, not an implementation of the presenter application.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json, validate_extraction
from graphify.cluster import cluster, score_all
from graphify.export import to_json
from graphify.report import generate


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "graphify-out"
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def source_files() -> list[Path]:
    """Use an explicit public-document boundary; never scan a data directory."""
    candidates = [ROOT / "README.md", ROOT / "AGENTS.md"]
    candidates.extend(sorted((ROOT / "docs").glob("*.md")))
    candidates.extend(sorted((ROOT / "docs" / "approaches").glob("*.md")))
    files = []
    for path in candidates:
        if not path.is_file() or path.is_symlink():
            continue
        if not path.resolve().is_relative_to(ROOT):
            raise ValueError("Document escaped project root")
        if any(parent.is_symlink() for parent in path.parents if parent != ROOT):
            raise ValueError("Document parent is a symlink")
        files.append(path)
    return files


def extract(files: list[Path]) -> tuple[dict, list[dict], int]:
    nodes, edges, coverage = [], [], []
    known = {path.resolve(): f"doc:{path.relative_to(ROOT).as_posix()}" for path in files}
    total_words = 0
    edge_keys = set()

    def add_edge(source: str, target: str, relation: str, file: str, line: int) -> None:
        key = (source, target, relation)
        if source == target or key in edge_keys:
            return
        edge_keys.add(key)
        edges.append({"source": source, "target": target, "relation": relation,
                      "confidence": "EXTRACTED", "source_file": file,
                      "source_location": f"L{line}", "_origin": "document_structure"})

    for path in files:
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")
        rel = path.relative_to(ROOT).as_posix()
        file_id = known[path.resolve()]
        coverage.append({"path": rel, "sha256": hashlib.sha256(raw).hexdigest()})
        total_words += len(text.split())
        nodes.append({"id": file_id, "label": rel, "file_type": "document",
                      "source_file": rel, "source_location": "L1",
                      "_origin": "document_structure"})
        stack = [(0, file_id)]
        fenced = False
        fence_char = ""
        for number, line in enumerate(text.splitlines(), 1):
            stripped = line.lstrip()
            if stripped.startswith(("```", "~~~")):
                marker = stripped[:3]
                if not fenced:
                    fenced, fence_char = True, marker
                elif marker == fence_char:
                    fenced = False
                continue
            if fenced:
                continue
            heading = HEADING.match(line)
            if heading:
                level, label = len(heading[1]), heading[2]
                while stack[-1][0] >= level:
                    stack.pop()
                node_id = f"{file_id}:section:{number}"
                nodes.append({"id": node_id, "label": label, "file_type": "concept",
                              "source_file": rel, "source_location": f"L{number}",
                              "_origin": "document_structure"})
                add_edge(stack[-1][1], node_id, "contains", rel, number)
                stack.append((level, node_id))
            for match in LINK.finditer(line):
                target = urlsplit(unquote(match[1].strip("<>")))
                if target.scheme or target.netloc or not target.path:
                    continue
                resolved = (path.parent / target.path).resolve()
                if resolved in known:
                    add_edge(stack[-1][1], known[resolved], "references", rel, number)

    extraction = {"nodes": nodes, "edges": edges, "hyperedges": [],
                  "input_tokens": 0, "output_tokens": 0}
    errors = validate_extraction(extraction)
    if errors:
        raise ValueError("Invalid extraction: " + "; ".join(errors[:5]))
    return extraction, coverage, total_words


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    files = source_files()
    if not files:
        raise ValueError("No approved documentary corpus")
    extraction, coverage, word_count = extract(files)
    graph = build_from_json(extraction, root=ROOT, directed=True, dedup=False)
    if graph.number_of_nodes() == 0:
        raise ValueError("Empty graph; refusing to overwrite outputs")
    # A heading/link graph is documentary scaffolding, not inferred architecture.
    graph.graph["scope"] = "planning_document_structure_only"
    graph.graph["extraction_method"] = "deterministic_markdown_headings_and_local_links"
    graph.graph["product_implemented"] = False
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    labels = {}
    for cid, members in communities.items():
        headings = [graph.nodes[n].get("label", n) for n in members
                    if graph.nodes[n].get("file_type") == "concept"]
        labels[cid] = headings[0] if headings else f"Documents {cid}"
    gods = god_nodes(graph)
    surprises = surprising_connections(graph, communities)
    questions = suggest_questions(graph, communities, labels)
    detection = {"total_files": len(files), "total_words": word_count,
                 "warning": "Documentary headings and explicit links only; no product code or semantic inference."}
    OUT.mkdir(exist_ok=True)
    if not to_json(graph, communities, str(OUT / "graph.json"), community_labels=labels):
        raise ValueError("Graphify shrink guard refused output; inspect changes before rebuilding")
    report = generate(graph, communities, cohesion, labels, gods, surprises,
                      detection, {"input": 0, "output": 0}, "Local Presenter",
                      suggested_questions=questions)
    preface = ("Documentary planning graph. Relationships are extracted from headings "
               "and explicit Markdown links, not inferred execution dependencies. "
               "No API/LLM was called for this graph build; input/output model tokens: 0/0. "
               "The separate planning agents have unmeasured token use.\n\n")
    (OUT / "GRAPH_REPORT.md").write_text(preface + report, encoding="utf-8")
    (OUT / "coverage.json").write_text(json.dumps({
        "schema": "local-presenter/document-graph-v1",
        "method": graph.graph["extraction_method"],
        "scope": graph.graph["scope"], "sources": coverage,
        "nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(),
        "input_tokens": 0, "output_tokens": 0,
        "semantic_extraction": False, "external_provider": False,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / ".graphify_analysis.json").write_text(json.dumps({
        "communities": communities, "cohesion": cohesion, "gods": gods,
        "surprises": surprises, "questions": questions,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / ".graphify_labels.json").write_text(json.dumps(labels, ensure_ascii=False), encoding="utf-8")
    print(f"Graphify: {len(files)} documents, {graph.number_of_nodes()} nodes, "
          f"{graph.number_of_edges()} edges, {len(communities)} communities.")
    print("No external model calls. Export the HTML with: graphify export html")


if __name__ == "__main__":
    main()
