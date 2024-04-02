from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_two_books_len(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Таня Гроттер')
        assert len(collector.books_genre) == 1
        assert 'Таня Гроттер' in collector.books_genre

    def test_add_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бумер')
        collector.add_new_book('Бумер')
        assert len(collector.books_genre) == 1

    def test_add_long_book_name(self):
        collector = BooksCollector()
        collector.add_new_book(
            'Длинное название книги, которое содержит больше 40 символов')
        assert 'Длинное название книги, которое содержит больше 40 символов' not in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга с жанром")
        collector.set_book_genre("Книга с жанром", "Фантастика")
        assert collector.get_book_genre("Книга с жанром") == "Фантастика"

    def test_set_book_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга с несуществующим жанром")
        collector.set_book_genre("Книга с несуществующим жанром", "Трагикомедия")
        assert collector.get_book_genre("Книга с жанром") is None

    @pytest.mark.parametrize("name, expected_genre", [("Книга1", "Ужасы"), ("Книга2", "Детективы")])
    def test_get_book_genre(self, name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Ужасы")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Детективы")
        assert collector.get_book_genre(name) == expected_genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Комедии")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Комедии")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Фантастика")
        assert collector.get_books_with_specific_genre("Комедии") == ["Книга1", "Книга2"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Мультфильмы")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Комедии")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга3", "Фантастика")
        assert collector.get_books_for_children() == ["Книга1", "Книга2", "Книга3"]

    def test_get_invalid_age_ratings_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Ужасы")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Детективы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.delete_book_from_favorites("Любимая книга")
        assert "Любимая книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_exact_match_search(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.add_new_book("Любимая книга детей")
        collector.add_book_in_favorites("Любимая книга детей")
        collector.delete_book_from_favorites("Любимая книга детей")
        assert "Любимая книга" in collector.get_list_of_favorites_books()
        assert "Любимая книга детей" not in collector.get_list_of_favorites_books()

    def test_get_books_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        collector.add_new_book("Любимая книга2")
        collector.add_book_in_favorites("Любимая книга2")

        assert "Любимая книга" and "Любимая книга2" in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 2