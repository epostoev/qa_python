import pytest


class TestBooksCollector:
    def test_add_new_book_add_one_book_success(self, collector):
        collector.add_new_book("50 оттенков серого")
        # input(f"\n{collector.books_genre}")
        assert collector.books_genre == {"50 оттенков серого": ""}

    def test_add_new_book_add_two_book_success(self, collector):
        collector.add_new_book("50 оттенков серого")
        collector.add_new_book("Старик и море")
        # input(f"\n{collector.books_genre}")
        assert collector.books_genre == {
            "50 оттенков серого": "", "Старик и море": ""}

    @pytest.mark.parametrize("name", ["A", "B" * 40])
    def test_add_new_book_valid_name_success(self, collector, name):
        collector.add_new_book(name)
        # input(f"\n{collector.get_books_genre()}")
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize("name", ["", "B" * 41])
    def test_add_new_book_invalid_name_length_41(self, collector, name):
        collector.add_new_book(name)
        # input(f"\n{collector.get_books_genre()}")
        assert name not in collector.get_books_genre()

    def test_set_book_genre_existing_genre(self, collector):
        collector.add_new_book("Форест Гамп")
        collector.set_book_genre("Форест Гамп", "Комедии")
        assert collector.get_book_genre("Форест Гамп") == "Комедии"

    def test_get_books_with_specific_genre_two_books_succsess(self, collector):
        collector.add_new_book("Зеленая миля")
        collector.add_new_book("Побег из Шоушенка")
        collector.set_book_genre("Зеленая миля", "Фантастика")
        collector.set_book_genre("Побег из Шоушенка", "Фантастика")
        # input(f"\n{collector.get_books_with_specific_genre("Фантастика")}")
        assert len(collector.get_books_with_specific_genre("Фантастика")) == 2

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Cмешарики")
        collector.add_new_book("Фреди Крюгер")
        collector.set_book_genre("Cмешарики", "Мультфильмы")
        collector.set_book_genre("Фреди Крюгер", "Ужасы")
        # input(f"\n {collector.get_books_for_children()}")
        assert collector.get_books_for_children() == ["Cмешарики"]

    def test_add_book_in_favorites_one_book_list_of_book(self, collector):
        collector.add_new_book("Форест Гамп")
        collector.add_book_in_favorites("Форест Гамп")
        assert collector.get_list_of_favorites_books() == ["Форест Гамп"]

    def test_add_book_in_favorites_one_book_not_in_list_of_book(
            self, collector):
        collector.add_new_book("Форест Гамп")
        collector.add_book_in_favorites("Чук и Гек")
        assert collector.get_list_of_favorites_books() not in ["Чук и Гек"]

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Форест Гамп")
        collector.add_book_in_favorites("Форест Гамп")
        collector.add_new_book("Смешарики")
        collector.add_book_in_favorites("Смешарики")
        collector.delete_book_from_favorites("Форест Гамп")
        assert ["Форест Гамп"] not in collector.get_list_of_favorites_books()

    def test_get_book_genre_non_existent_book(self, collector):
        assert collector.get_book_genre('Несуществующая') is None
