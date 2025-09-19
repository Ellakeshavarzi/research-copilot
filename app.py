# =========================
# app.py (Streamlit UI)
# =========================


import streamlit as st
from settings import USE_LOCAL, TOP_K
from ingest import build_or_load_index
from utils import retrieve_with_citations


# LLMs for LangChain side
if USE_LOCAL:
    from langchain_ollama import ChatOllama
    llm = ChatOllama(model="llama3.1:8b", temperature=0.2)
else:
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


from chains import build_chain


st.set_page_config(page_title="Research Copilot", layout="wide")
st.title("📚 Research Copilot — RAG with Citations")


st.sidebar.header("Index Controls")
rebuild = st.sidebar.button("Rebuild Index")


with st.spinner("Loading/Building index…"):
    index = build_or_load_index()


chain = build_chain(llm)


if rebuild:
    st.success("Index refreshed. (Re-run if you just added PDFs to /data)")


st.markdown("Upload PDFs to the `data/` folder, then ask questions below.")
q = st.text_input("Ask about your documents")
ask = st.button("Ask")


if ask and q:
    with st.spinner("Retrieving + generating answer…"):
        context, nodes = retrieve_with_citations(index, q, k=TOP_K)
        answer = chain.invoke({"question": q, "context": context})


st.subheader("Answer")
st.write(answer)


st.subheader("Sources")
for n in nodes:
    meta = n.node.metadata or {}
    title = meta.get("file_name", "Document")
    page = meta.get("page_label", meta.get("page", "?"))
    st.write(f"- **{title}**, p.{page}")

