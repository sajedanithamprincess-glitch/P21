import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader, Docx2txtLoader


class DocumentLoader:
    def __init__(self, docs_path):
        self.docs_path = docs_path

    def load(self):
        if not os.path.exists(self.docs_path):
            raise FileNotFoundError(f"The directory '{self.docs_path}' does not exist.")

        documents = []

        loaders = [
            DirectoryLoader(self.docs_path, glob="**/*.txt", loader_cls=TextLoader, silent_errors=True),
            DirectoryLoader(self.docs_path, glob="**/*.pdf", loader_cls=PyPDFLoader, silent_errors=True),
            DirectoryLoader(self.docs_path, glob="**/*.docx", loader_cls=Docx2txtLoader, silent_errors=True),
        ]

        for loader in loaders:
            documents.extend(loader.load())

        if not documents:
            raise FileNotFoundError("No supported files found in docs folder.")

        return documents