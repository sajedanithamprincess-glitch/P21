from langchain_core.documents import Document
from src.rag_pipeline import RAGPipeline


class FakeVectorStore:
    def similarity_search_with_score(self, query, k=5):
        return [
            (
                Document(
                    page_content="Google was founded in 1998.",
                    metadata={"source": "google.txt", "page": 1}
                ),
                0.1234
            )
        ]


class FakeLLMService:
    def generate_answer(self, query, context_text):
        assert "Google was founded in 1998." in context_text
        assert "google.txt" in context_text
        return "Google was founded in 1998. (Source: google.txt, Page: 1)"


def test_rag_pipeline_returns_answer():
    vector_store = FakeVectorStore()
    llm_service = FakeLLMService()

    rag = RAGPipeline(vector_store, llm_service, top_k=5)

    answer = rag.ask("When was Google founded?")

    assert "1998" in answer
    assert "google.txt" in answer