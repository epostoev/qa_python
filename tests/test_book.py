import pytest
import data


class TestBooksCollector:
    def test_add_new_book_add_one_book_success(self, collector):
        collector.add_new_book(data.BOOK_5)
        assert collector.books_genre == {data.BOOK_5: ""}

    def test_add_new_book_add_two_book_success(self, collector):
        collector.add_new_book(data.BOOK_5)
        collector.add_new_book(data.BOOK_6)
        assert collector.books_genre == {
            data.BOOK_5: "", data.BOOK_6: ""}

    @pytest.mark.parametrize("name", ["A", "B" * 40])
    def test_add_new_book_valid_name_success(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize("name", ["", "B" * 41])
    def test_add_new_book_invalid_name_length_41(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre_existing_genre(self, collector):
        collector.add_new_book(data.BOOK_2)
        collector.set_book_genre(data.BOOK_2, "Комедии")
        assert collector.get_book_genre(data.BOOK_2) == "Комедии"

    def test_get_books_with_specific_genre_two_books_succsess(self, collector):
        collector.add_new_book(data.BOOK_3)
        collector.add_new_book(data.BOOK_4)
        collector.set_book_genre(data.BOOK_3, "Фантастика")
        collector.set_book_genre(data.BOOK_4, "Фантастика")
        assert len(collector.get_books_with_specific_genre("Фантастика")) == 2

    def test_get_books_for_children(self, collector):
        collector.add_new_book(data.BOOK_1)
        collector.add_new_book(data.BOOK_2)
        collector.set_book_genre(data.BOOK_1, "Мультфильмы")
        collector.set_book_genre(data.BOOK_2, "Ужасы")
        assert collector.get_books_for_children() == [data.BOOK_1]

    def test_add_book_in_favorites_one_book_list_of_book(self, collector):
        collector.add_new_book(data.BOOK_2)
        collector.add_book_in_favorites(data.BOOK_2)
        assert collector.get_list_of_favorites_books() == [data.BOOK_2]

    def test_add_book_in_favorites_one_book_not_in_list_of_book(
            self, collector):
        collector.add_new_book(data.BOOK_2)
        collector.add_book_in_favorites(data.BOOK_7)
        assert collector.get_list_of_favorites_books() not in [data.BOOK_7]

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book(data.BOOK_2)
        collector.add_book_in_favorites(data.BOOK_2)
        collector.add_new_book(data.BOOK_1)
        collector.add_book_in_favorites(data.BOOK_1)
        collector.delete_book_from_favorites(data.BOOK_2)
        assert [data.BOOK_2] not in collector.get_list_of_favorites_books()

    def test_get_book_genre_non_existent_book(self, collector):
        assert collector.get_book_genre('Несуществующая') is None

    def test_get_books_genre(self, collector):
        collector.add_new_book(data.BOOK_7)
        collector.set_book_genre(data.BOOK_7, "Мультфильмы")
        result = collector.get_books_genre()
        assert isinstance(result, dict) and result == {
            data.BOOK_7: "Мультфильмы"}
