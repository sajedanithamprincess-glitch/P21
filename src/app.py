from dotenv import load_dotenv
from src.config import PERSIST_DIRECTORY, EMBEDDING_MODEL, LLM_MODEL, TOP_K
from src.vector_store_service import VectorStoreService
from src.llm_service import LLMService
from src.rag_pipeline import RAGPipeline


def main():
    load_dotenv()

    vector_store_service = VectorStoreService(PERSIST_DIRECTORY, EMBEDDING_MODEL)
    vector_store = vector_store_service.load()

    llm_service = LLMService(LLM_MODEL)
    rag = RAGPipeline(vector_store, llm_service, TOP_K)

    print("\nRAG Assistant Ready")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer = rag.ask(query)

        print("\n--- AI Answer ---\n")
        print(answer)
        print("\n" + "-" * 70 + "\n")


if __name__ == "__main__":
    main()