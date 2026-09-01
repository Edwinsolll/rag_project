# RAG-Based Document Q&A System

A document-based question-answering system that uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-grounded answers using an LLM.

## Current Features

- PDF text extraction and chunking
- Sentence Transformer embeddings
- Semantic retrieval using ChromaDB
- Groq-hosted Llama for answer generation
- FastAPI REST API
- Pydantic request validation
- PostgreSQL database integration
- User registration and login
- Password hashing with Argon2
- JWT authentication
- Logging and error handling

## Architecture

PDF

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Relevant Context

↓

Groq / Llama

↓

Generated Answer

## Backend

FastAPI handles the API layer, while PostgreSQL stores application data such as users and document metadata.

## Authentication

The application supports user registration and login using password hashing and JWT-based authentication.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- ChromaDB
- Sentence Transformers
- Groq
- LangChain
- Git / GitHub

## Future Improvements

- Metadata filtering
- Hybrid search
- Reranking
- Query rewriting
- Source citations
- Retrieval evaluation
- Conversation memory
- Automated testing with pytest
- Docker
- Cloud deployment