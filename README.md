# PARA — PDF-Augmented Retrieval Assistant

PARA (PDF-Augmented Retrieval Assistant) is a simple Retrieval-Augmented Generation (RAG) chatbot that answers questions using information retrieved from a PDF document.

## Workflow

```text
PDF Document
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Sentence Transformer Embeddings
    ↓
FAISS Vector Index
    ↓
Question Embedding
    ↓
Relevant Chunk Retrieval
    ↓
Phi-3 LLM
    ↓
Answer
```

## Repository Contents

This **PARA** repository contains both **Jupyter Notebook (`.ipynb`) and Python (`.py`) files**.

- `pdf_related_chatbot_with_RAG.ipynb` — Complete RAG chatbot workflow in notebook format.
- `src/` — Python implementation separated into modules following the notebook's code sequence.

## Python Modules

```text
src/
├── 01_installation.py
├── 02_imports.py
├── 03_pdf_upload.py
├── 04_pdf_extraction.py
├── 05_text_chunking.py
├── 06_embedding_and_faiss.py
├── 07_llm_setup.py
└── 08_rag_chatbot.py
```

## Technologies

- Python
- PyPDF
- Sentence Transformers
- FAISS
- NumPy
- Hugging Face Transformers
- Phi-3 Mini
- Google Colab
- Retrieval-Augmented Generation (RAG)

## Key Concepts

The project demonstrates a basic RAG pipeline: PDF content is extracted and divided into fixed-size chunks, embeddings are generated using `all-MiniLM-L6-v2`, and the embeddings are indexed with FAISS. A user's question is embedded and the most similar chunk is retrieved before being provided to the Phi-3 Mini language model.

## Purpose

PARA is a learning-focused project for understanding the fundamental components of a PDF-based RAG chatbot, from document ingestion and chunking to vector retrieval and LLM-based answer generation.

## Note

The original notebook is designed for Google Colab and uses `files.upload()` for PDF input. The Python modules preserve the notebook's implementation and execution sequence for learning and experimentation.
