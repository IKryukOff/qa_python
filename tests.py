import pytest
from data import book_name_for_test
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book(self, collector: BooksCollector):
        collector.add_new_book('Задача трех тел')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['',
                                      'Book with name langth more than 40 letters'])
    def test_add_new_book_invalid_length(self, collector: BooksCollector,
                                         name: str):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre',
                             [['Задача трех тел', 'Фантастика'],
                              ['Сияние', 'Ужасы'],
                              ['Недоросль', 'Комедии']])
    def test_set_book_genre(self, collector: BooksCollector,
                            name: str,
                            genre: str):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_book(self, collector: BooksCollector):
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.set_book_genre('Дядя Федор, кот и пес', 'Мультфильмы')
        assert collector.get_book_genre('Дядя Федор, кот и пес') is None

    @pytest.mark.parametrize('name, genre',
                             [['Задача трех тел', 'Мистика'],
                              ['Сияние', 'Сатира'],
                              ['Недоросль', 'Технологии']])
    def test_set_book_genre_invalid_genre(self, collector: BooksCollector,
                                          name: str,
                                          genre: str):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('name, genre',
                             [['Солярис', 'Фантастика'],
                              ['Мизери', 'Ужасы'],
                              ['Недоросль', 'Комедии']])
    def test_get_book_genre(self, collector: BooksCollector,
                            name: str,
                            genre: str,
                            fillup_collector):
        assert collector.get_book_genre(name) == genre

    def test_get_books_genre(self, collector: BooksCollector,
                             fillup_collector):
        assert len(collector.get_books_genre()) == 9

    @pytest.mark.parametrize('name, is_for_children',
                             [['Дракула', False],
                              ['Мама для мамонтенка', True],
                              ['Дядя Федор, пес и кот', True],
                              ['Лунный камень', False]])
    def test_get_books_for_children_book_is_for_children(self,
                                                         collector: BooksCollector,
                                                         name: str,
                                                         is_for_children: bool,
                                                         fillup_collector):
        assert (name in collector.get_books_for_children()) == is_for_children

    def test_add_book_in_favorites(self, collector: BooksCollector,
                                   fillup_collector):
        collector.add_book_in_favorites(book_name_for_test)
        favorite_books = collector.get_list_of_favorites_books()
        assert (len(favorite_books) != 0 and book_name_for_test in favorite_books)

    def test_add_book_in_favorites_not_exist(self, collector: BooksCollector):
        collector.add_book_in_favorites(book_name_for_test)
        favorite_books = collector.get_list_of_favorites_books()
        assert (book_name_for_test not in favorite_books)

    def test_get_list_of_favorites_books(self, collector: BooksCollector,
                                         fillup_collector):
        collector.add_book_in_favorites(book_name_for_test)
        assert collector.get_list_of_favorites_books() == [book_name_for_test]

    def test_delete_book_from_favorites(self, collector: BooksCollector,
                                        fillup_collector):
        collector.add_book_in_favorites(book_name_for_test)
        collector.delete_book_from_favorites(book_name_for_test)
        assert book_name_for_test not in collector.get_list_of_favorites_books()
