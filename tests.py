from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_books_first_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Титаник')
        assert collector.get_book_rating('Титаник') == 1

    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_rating()) == 1

    import pytest
    @pytest.mark.parametrize('rating', [0, 11])
    def test_set_book_rating_cant_set_rating_less_and_greater_range(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Робинзон Крузо')
        collector.set_book_rating('Робинзон Крузо',rating)
        assert collector.get_book_rating('Робинзон Крузо') == 1

    def test_get_book_rating_absent_book_no_rating(self):
        collector = BooksCollector()
        rating = collector.get_book_rating('Война и мир')
        assert rating is None

    def test_get_books_with_specific_rating_one(self):
        collector = BooksCollector()
        collector.add_new_book('Великий Гэтсби')
        collector.add_new_book('Робинзон Крузо')
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Мастер и маргарита', 5)
        result = collector.get_books_with_specific_rating(1)
        assert result == ['Великий Гэтсби','Робинзон Крузо']

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Записки охотника')
        assert collector.get_books_rating() == {'Записки охотника': 1}

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сумерки')
        collector.add_book_in_favorites('Сумерки')
        assert collector.get_list_of_favorites_books() == ['Сумерки']

    def test_add_to_favorites_fails_if_not_in_ratings(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Мцыри')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Каштанка')
        collector.add_book_in_favorites('Каштанка')
        collector.delete_book_from_favorites('Каштанка')
        assert collector.get_list_of_favorites_books() == []
