# 🏢 AI Knowledge Assistant - Company Policy Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4.22+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## 📌 Project Overview

An intelligent document chatbot that answers employee questions about company policies using **Retrieval Augmented Generation (RAG)** and **Semantic Search**. Instead of generic AI answers, this assistant reads your actual company documents and provides accurate, context-aware responses.

### 🎯 Problem Statement

Companies have thousands of internal documents (policies, handbooks, benefits guides) that are difficult to search. Employees waste time searching through PDFs or asking HR repetitive questions.

### 💡 Solution

This AI-powered assistant:
- ✅ Reads your company documents
- ✅ Understands questions in natural language
- ✅ Finds relevant information using semantic search
- ✅ Provides accurate answers with source tracking

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📄 **Document Processing** | Loads and chunks text files (500 chars, 50 overlap) |
| 🔍 **Semantic Search** | Finds documents by **meaning**, not exact keywords |
| 🧠 **Embeddings** | Converts text to 768-dim vectors using sentence-transformers |
| 🗄️ **Vector Database** | ChromaDB for efficient similarity search |
| 💬 **Chat Interface** | Streamlit web UI with conversation history |
| 📊 **Source Tracking** | Shows which policy document provided the answer |

---

## 🎬 Live Demo

> **URL:** `https://your-username.streamlit.app` (after deployment)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain |
| **Embeddings** | Sentence-Transformers (all-mpnet-base-v2) |
| **Vector DB** | ChromaDB |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure
