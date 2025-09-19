# =========================
# ingest.py
# =========================


import os
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
from settings import CHUNK_SIZE, CHUNK_OVERLAP


DATA_DIR = "data"
DB_DIR = "storage/chroma"
COLLECTION_NAME = "docs"




def get_vector_store():
    os.makedirs(DB_DIR, exist_ok=True)
    client = chromadb.PersistentClient(DB_DIR)
    collection = client.get_or_create_collection(COLLECTION_NAME)
    return ChromaVectorStore(chroma_collection=collection)




def build_or_load_index():
    """Create the vector store (if empty), then return an Index bound to it."""
    vector_store = get_vector_store()


    # If the collection is empty, (re)ingest
    # Chroma doesn't expose count directly via API wrapper; try loading docs regardless
    docs = []
    if any(fname.lower().endswith(".pdf") for fname in os.listdir(DATA_DIR)):
        docs = SimpleDirectoryReader(DATA_DIR, required_exts=[".pdf"]).load_data()


    if docs:
        splitter = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        nodes = splitter.get_nodes_from_documents(docs)
        index = VectorStoreIndex(nodes, vector_store=vector_store)
    else:
        # No new docs—bind index to existing vector store
        index = VectorStoreIndex.from_vector_store(vector_store)


    return index




if __name__ == "__main__":
    idx = build_or_load_index()
    print("Index ready.")

