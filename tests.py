import pytest
from main import BooksCollector


class TestBooksCollector:
    # создаем новый экземпляр BooksCollector перед каждым тестом
    @pytest.fixture(autouse=True)
    def setup_colector(self):
        self.collector = BooksCollector()

    # заполняем self.collector тестовыми данными
    @pytest.fixture
    def fillup_collector(self):
        self.collector.books_genre['Дракула'] = 'Ужасы'
        self.collector.books_genre['Мама для мамонтенка'] = 'Мультфильмы'
        self.collector.books_genre['Солярис'] = 'Фантастика'
        self.collector.books_genre['Война миров'] = 'Фантастика'
        self.collector.books_genre['Задача трех тел'] = 'Фантастика'
        self.collector.books_genre['Недоросль'] = 'Комедии'
        self.collector.books_genre['Лунный камень'] = 'Детективы'
        self.collector.books_genre['Мизери'] = 'Ужасы'
        self.collector.books_genre['Дядя Федор, пес и кот'] = 'Мультфильмы'

    @pytest.fixture
    def book_name_for_test(self):
        return 'Солярис'

    def test_add_new_book(self):
        self.collector.add_new_book('Задача трех тел')
        assert len(self.collector.get_books_genre()) == 1

    def test_add_new_book_invalid_length(self):
        self.collector.add_new_book('')
        self.collector.add_new_book('Book with name langth more than 40 letters')
        assert len(self.collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre',
                             [['Задача трех тел', 'Фантастика'],
                              ['Сияние', 'Ужасы'],
                              ['Недоросль', 'Комедии']])
    def test_set_book_genre(self, name, genre):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_book(self):
        self.collector.add_new_book('Дядя Федор, пес и кот')
        self.collector.set_book_genre('Дядя Федор, кот и пес', 'Мультфильмы')
        assert self.collector.get_book_genre('Дядя Федор, кот и пес') is None

    @pytest.mark.parametrize('name, genre',
                             [['Задача трех тел', 'Мистика'],
                              ['Сияние', 'Сатира'],
                              ['Недоросль', 'Технологии']])
    def test_set_book_genre_invalid_genre(self, name, genre):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert self.collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name, genre',
                             [['Солярис', 'Фантастика'],
                              ['Мизери', 'Ужасы'],
                              ['Недоросль', 'Комедии']])
    def test_get_book_genre(self, name, genre, fillup_collector):
        assert self.collector.get_book_genre(name) == genre

    def test_get_books_genre(self, fillup_collector):
        assert len(self.collector.get_books_genre()) == 9

    @pytest.mark.parametrize('name, is_for_children',
                             [['Дракула', False],
                              ['Мама для мамонтенка', True],
                              ['Дядя Федор, пес и кот', True],
                              ['Лунный камень', False]])
    def test_get_books_for_children_book_is_for_children(self,
                                                         name,
                                                         is_for_children,
                                                         fillup_collector):
        assert (name in self.collector.get_books_for_children()) == is_for_children

    def test_add_book_in_favorites(self, fillup_collector, book_name_for_test):
        self.collector.add_book_in_favorites(book_name_for_test)
        favorite_books = self.collector.get_list_of_favorites_books()
        assert (len(favorite_books) != 0 and book_name_for_test in favorite_books)

    def test_add_book_in_favorites_not_exist(self, book_name_for_test):
        self.collector.add_book_in_favorites(book_name_for_test)
        favorite_books = self.collector.get_list_of_favorites_books()
        assert (book_name_for_test not in favorite_books)

    def test_delete_book_from_favorites(self, fillup_collector, book_name_for_test):
        self.collector.add_book_in_favorites(book_name_for_test)
        assert book_name_for_test in self.collector.get_list_of_favorites_books()
        self.collector.delete_book_from_favorites(book_name_for_test)
        assert book_name_for_test not in self.collector.get_list_of_favorites_books()
