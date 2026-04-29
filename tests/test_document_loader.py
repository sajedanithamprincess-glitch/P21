import pytest
from src.document_loader import DocumentLoader


def test_document_loader_raises_error_for_missing_folder():
    loader = DocumentLoader("folder_that_does_not_exist")

    with pytest.raises(FileNotFoundError):
        loader.load()