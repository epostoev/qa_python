from main import BooksCollector
import pytest


@pytest.fixture(scope="function")
def collector():
    return BooksCollector()
