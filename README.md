# 🏗️ Software Architecture & SOLID Refactoring

In this project, I evolved the functional prototype from Project 1 into a robust, maintainable, and flexible software application. My primary goal was to "pay down technical debt" by transitioning from a script-based approach to a modular architecture guided by **SOLID principles**.

---

## 🔴 The Problem: Technical Debt in Project 1
In my initial implementation, the system was "tightly coupled" and followed a monolithic script structure:
* **Monolithic Files:** I only had `ingestion.py` and `retrieval.py`, where each file performed 4-5 distinct tasks (loading, splitting, embedding, searching, and generating).
* **Brittleness:** Changing one part of the code (like the chunking strategy) risked breaking unrelated parts (like the database connection).
* **Rigidity:** The code was "married" to specific tools like OpenAI and ChromaDB, making it difficult to test or swap models.

---

## 🟢 The Solution: Applying SOLID Principles

To improve this, I refactored the project using two core pillars of software design:

### 1. Single Responsibility Principle (SRP)
I broke the "God Files" into five specialized services. Each class now has **one reason to change**.

| Component | Responsibility |
| :--- | :--- |
| **`DocumentLoader`** | Extracting raw text from the `/docs` directory. |
| **`TextSplitterService`** | Mathematical logic for chunking and overlapping text. |
| **`VectorStoreService`** | Interfacing with ChromaDB (Storage & Retrieval). |
| **`LLMService`** | Managing prompt templates and OpenAI API interactions. |
| **`RAGPipeline`** | The "Orchestrator" that coordinates the flow of data between services. |

**Impact:** Debugging is now surgical. If a document fails to load, I know the error is isolated to the `DocumentLoader`, leaving the LLM and Database logic untouched.

### 2. Dependency Inversion Principle (DIP)
I decoupled the high-level logic from the low-level tools. Instead of the `RAGPipeline` creating its own tools, it now **receives** them through **Dependency Injection**.

* **Before:** The pipeline was hardcoded to use `ChatOpenAI`.
* **After:** The pipeline expects a generic "Generator Service." This means I can "inject" an OpenAI service today and a local **LLaMA 3.1** service tomorrow without changing a single line of the pipeline's core logic.

---

## 🚀 Impact on Maintainability
This refactor has moved the project from a "student script" to an "industry-ready" application:
* **Scalability:** I can add support for new file types just by adding a new Loader class.
* **Testability:** I can now write unit tests for the `TextSplitterService` without needing to call the OpenAI API, saving time and costs.
* **Flexibility:** The system is now provider-agnostic. We are no longer locked into one vendor for embeddings or LLM generation.

run 
`
python -m src.ingest_app 
`
then run
`
 python -m src.app    
`


## Testing with Pytest

I used pytest to test the refactored RAG pipeline. The tests verify the main components of the system, including document loading, text splitting, and the RAG pipeline.

I also used fake vector store and fake LLM service objects to test the pipeline without calling the OpenAI API. This makes the tests faster, repeatable, and independent from external services.

run 
`
pip install pytest
`
then run
`
python -m pytest
`
last
`
htmlcov/index.html
`# p2
# p2
# P21
# P21
# P21
# P21
