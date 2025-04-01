import pytest
from data import books_with_genres_for_fillup
from main import BooksCollector


@pytest.fixture
def collector() -> BooksCollector:
    return BooksCollector()


@pytest.fixture
def fillup_collector(collector: BooksCollector):
    for name, genre in books_with_genres_for_fillup:
        collector.books_genre[name] = genre
