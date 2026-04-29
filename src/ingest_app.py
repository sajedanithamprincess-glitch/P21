import os
from dotenv import load_dotenv

from src.config import DOCS_PATH, PERSIST_DIRECTORY, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP
from src.document_loader import DocumentLoader
from src.text_splitter_service import TextSplitterService
from src.vector_store_service import VectorStoreService


def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY was not found.")

    loader = DocumentLoader(DOCS_PATH)
    splitter = TextSplitterService(CHUNK_SIZE, CHUNK_OVERLAP)
    vector_store_service = VectorStoreService(PERSIST_DIRECTORY, EMBEDDING_MODEL)

    documents = loader.load()
    chunks = splitter.split(documents)
    vector_store_service.create(chunks)

    print("Ingestion complete.")


if __name__ == "__main__":
    main()