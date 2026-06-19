# AI-Powered Customer Support RAG Agent

An end-to-end Retrieval-Augmented Generation (RAG) system that enables intelligent customer support by answering questions from enterprise documents with citation-backed responses. The application leverages Google Gemini, LangChain, FAISS, FastAPI, and Streamlit to provide accurate, context-aware, and scalable document question-answering capabilities.

---

## 🚀 Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using FAISS vector database
* 🤖 Context-aware responses powered by Google Gemini
* 📚 Retrieval-Augmented Generation (RAG) architecture
* 📝 Citation-backed answers to reduce hallucinations
* 💬 Conversational memory for multi-turn interactions
* ⚡ FastAPI backend with REST APIs
* 🎨 Interactive Streamlit user interface
* 🐳 Dockerized deployment
* 🏗️ Modular and scalable codebase

---

## 🛠️ Tech Stack

### AI & LLM

* Google Gemini API
* LangChain

### Retrieval & Vector Search

* FAISS
* Embeddings

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### Deployment

* Docker

---

## 🏗️ System Architecture

```text
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Prompt Construction
      │
      ▼
Google Gemini
      │
      ▼
Citation-Based Response
```

---

## 📂 Project Structure

```text
customer-support-rag-agent/
│
├── api/                    # FastAPI routes and APIs
├── rag/                    # RAG pipeline components
├── utils/                  # Utility functions
├── data/                   # Sample documents
├── vectordb/               # Generated vector database
│
├── app.py                  # Streamlit application
├── config.py               # Configuration settings
├── Dockerfile              # Docker configuration
├── requirements.txt        # Dependencies
├── README.md
│
└── tests/                  # Testing scripts
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/thevaibhavsengar/customer-support-rag-agent.git
cd customer-support-rag-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

---

## ▶️ Running the Application

### Start the Streamlit UI

```bash
streamlit run app.py
```

### Start the FastAPI Backend

```bash
uvicorn api.main:app --reload
```

---

## 🐳 Docker Deployment

Build the Docker image:

```bash
docker build -t customer-support-rag-agent .
```

Run the container:

```bash
docker run -p 8501:8501 customer-support-rag-agent
```

---

## 📸 Screenshots

Add screenshots of:

* PDF Upload Interface
* Chat Interface
* Citation-Based Responses
* FastAPI Documentation

Example:

```markdown
![Home Page](assets/home.png)
![Chat Interface](assets/chat.png)
```

---

## 🎯 Key Highlights

* Developed a complete Retrieval-Augmented Generation pipeline.
* Implemented semantic search using FAISS vector indexing.
* Reduced hallucinations through context-grounded retrieval.
* Built a scalable FastAPI backend with modular architecture.
* Enabled conversational interactions with memory support.
* Containerized the application using Docker.

---

## 🔮 Future Enhancements

* Multi-document collections
* Hybrid search (BM25 + Vector Search)
* User authentication and role management
* Support for DOCX and TXT files
* Chat history persistence
* Cloud deployment (AWS/GCP/Azure)

---

## 👨‍💻 Author

**Vaibhav Sengar**

* GitHub: https://github.com/thevaibhavsengar
* LinkedIn: linkedin.com/in/thevaibhavsengar

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
