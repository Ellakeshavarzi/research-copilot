#  Research Copilot — RAG with Citations  

A lightweight **Retrieval-Augmented Generation (RAG)** app built with **LlamaIndex** and **LangChain**.  
Upload PDFs (research papers, lecture notes, standards), then ask natural questions.  
You’ll get concise answers with **page-level citations**.  

---

## Features
-  **Ask any question** across multiple PDFs.  
-  **Citations**: every answer cites sources like `[Doc, p.X]`.  
-  **Local or Cloud LLMs**:  
  - **Local** with [Ollama](https://ollama.ai/) (`llama3.1:8b`)  
  - **Hosted** with OpenAI (`gpt-4o-mini`)  
-  **Easy ingestion**: just drop PDFs into `data/`.  
-  **Simple UI**: Streamlit frontend.  
-  **Optional eval** with [Ragas](https://github.com/explodinggradients/ragas) for RAG quality checks.  

---

## Tech Stack
- [LlamaIndex](https://docs.llamaindex.ai/) → ingestion, chunking, retrieval  
- [LangChain](https://www.langchain.com/) → prompting & orchestration  
- [ChromaDB](https://www.trychroma.com/) → vector storage  
- [Streamlit](https://streamlit.io/) → interactive UI  
- [Ollama](https://ollama.ai/) or [OpenAI](https://openai.com/) → LLM backend  

---

## Project Structure
research-copilot/
- ├─ app.py # Streamlit UI
- ├─ ingest.py # Ingest PDFs & build index
- ├─ chains.py # LangChain RAG chain
- ├─ settings.py # Model + embedding config
- ├─ utils.py # Retrieval helper (citations)
- ├─ requirements.txt # Python deps
- ├─ environment.yml # Conda env (optional)
- ├─ data/ # Put your PDFs here
- └─ storage/ # Auto-created for vector DB


---

## Getting Started

### 1. Clone repo
```bash
git clone https://github.com/YOURNAME/research-copilot.git
cd research-copilot
```
### 2. Create environment (Anaconda)
```
conda create -n researchcopilot python=3.11 -y
conda activate researchcopilot
```
### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Add your PDFs

Place documents into the data/ folder.

### 5. Run the app
```
streamlit run app.py
```

### 6. Choose your LLM

Local → install Ollama, then:
```
ollama pull llama3.1:8b
```

Set ```USE_LOCAL = True``` in settings.py.

Cloud → export your OpenAI API key:

```
export OPENAI_API_KEY=sk-...
```


Set ```USE_LOCAL = False``` in settings.py.


### License

MIT — feel free to use and adapt.