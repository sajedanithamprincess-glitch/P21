from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


class VectorStoreService:
    def __init__(self, persist_directory, embedding_model_name):
        self.persist_directory = persist_directory
        self.embedding_model = OpenAIEmbeddings(model=embedding_model_name)

    def create(self, chunks):
        return Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )

    def load(self):
        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )