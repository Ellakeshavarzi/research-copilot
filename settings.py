# =========================
# settings.py
# =========================


USE_LOCAL = True # set False if you want to use OpenAI


# Global config for LlamaIndex models
from llama_index.core import Settings


if USE_LOCAL:
    # Local via Ollama
    from llama_index.llms.ollama import Ollama
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding


    Settings.llm = Ollama(model="llama3.1:8b", request_timeout=120)
    Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
else:
    import os
    from llama_index.llms.openai import OpenAI
    from llama_index.embeddings.openai import OpenAIEmbedding


    # Make sure your OPENAI_API_KEY is exported in your shell
    Settings.llm = OpenAI(model="gpt-4o-mini")
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")


# Retrieval tuning
TOP_K = 4
CHUNK_SIZE = 850
CHUNK_OVERLAP = 120