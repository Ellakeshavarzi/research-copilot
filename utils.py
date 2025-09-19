# =========================
# utils.py
# =========================


from typing import List, Tuple
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever




def retrieve_with_citations(index: VectorStoreIndex, q: str, k: int) -> Tuple[str, List]:
    """Return a compact context string + raw nodes for UI display."""
    retriever = VectorIndexRetriever(index=index, similarity_top_k=k)
    nodes = retriever.retrieve(q)
    ctx_lines = []
    for n in nodes:
        meta = n.node.metadata or {}
        title = meta.get("file_name", "Document")
        page = meta.get("page_label", meta.get("page", "?"))
        # Safe slice of content, avoiding super long chunks in the prompt
        content = n.node.get_content()
        if len(content) > 900:
            ontent = content[:900] + "…"
        ctx_lines.append(f"[{title}, p.{page}] {content}")
    return "\n\n".join(ctx_lines), nodes

