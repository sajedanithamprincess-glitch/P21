from langchain_core.documents import Document
from src.text_splitter_service import TextSplitterService


def test_split_documents_creates_chunks():
    documents = [
        Document(page_content="This is a test document. " * 100)
    ]

    splitter = TextSplitterService(chunk_size=100, chunk_overlap=10)
    chunks = splitter.split(documents)

    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 100 for chunk in chunks)