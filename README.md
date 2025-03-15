1. test_add_new_book: проверяет добавление новой книги.
2. test_add_new_book_invalid_length: проверяет, что книги не добавляются, если имя пустое или превышает 40 символов.
3. test_set_book_genre: проверяет корректную установку жанра книги.
4. test_set_book_genre_invalid_book: проверяет, что нельзя установить жанр несуществующим книгам.
5. test_set_book_genre_invalid_genre: проверяет, что нельзя установить несуществующий жанр.
6. test_get_book_genre: проверяет, что правильно возвращается жанр для указанной книги.
7. test_get_books_genre: проверяет возврат всего словаря книг.
8. test_get_books_for_children_book_is_for_children: проверяет, что возвращаются только доступные детям книги.
9. test_add_book_in_favorites: проверяет добавление книги в избранное.
10. test_add_book_in_favorites_not_exist: проверяет, что нельзя добавить несуществующую книгу в избранное.
11. test_delete_book_from_favorites: проверяет возможность удаления книги из избранного