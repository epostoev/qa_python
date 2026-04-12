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
