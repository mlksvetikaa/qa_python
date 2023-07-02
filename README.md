# qa_python

test_add_new_book_books_first_rating 
# проверяем, что при добавлении книги, ей присваевается рейтиг 1
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# проверяем, что рейтинг равен 1
# PASSED 

test_add_new_book_add_one_book_twice
# проверяем, что нельзя добавить одну и ту же книгу дважды
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# снова добавляем книгу с этим же именем
# проверяем, что книга добавилась только один раз
# PASSED 

test_set_book_rating_cant_add_rating_missing_book
# проверяем, что с ошибкой в названии книге рейтинг не присваивается
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# устанавливаем рейтинг книге с ошибкой - 5
# проверяем, что рейтинг книги не поменялся
# PASSED 

test_set_book_rating_cant_set_rating_less_than_1
# проверяем, что нельзя выставить рейтинг меньше 1
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# устанавливаем рейтинг книге - 0
# проверяем, что рейтинг книги не поменялся
# PASSED 

test_set_book_rating_cant_set_rating_greater_than_10
# проверяем, что нельзя выставить рейтинг больше 10
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# устанавливаем рейтинг книге - 11
# проверяем, что рейтинг книги не поменялся
# PASSED 

test_get_book_rating_absent_book_no_rating
# проверяем, что у недобавленной книги нет рейтинга
# создаем экземпляр (объект) класса BooksCollector
# проверяем, что рейтинг не выводится, потому что пропущено добавление книги
# PASSED 

test_get_books_with_specific_rating_one
# выводим список книг с определенным рейтингом
# создаем экземпляр (объект) класса BooksCollector
# добавляем три книги
# устанавливаем рейтинг третьей книге 
# выводим список книг с рейтингом 1
# FAILED
# О.Р. - выведены книги с рейтийнгом 1
# Ф.Р. - выведены все книги

test_get_books_rating
# проверяем добавление книги в словарь
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# проверяем добавилась ли книга в словарь
# PASSED 

test_add_book_in_favorites
# проверяем добавление книги в избранное
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# добавляем книгу в избранное
# проверяем наличие книги в списке избранного
# PASSED 

test_add_to_favorites_fails_if_not_in_ratings
# проверяем, что нельзя добавить книгу в избранное, если ее нет в словаре
# создаем экземпляр (объект) класса BooksCollector
# добавляем книгу в избранное без добавления в словарь
# проверяем список избранного - он пуст
# PASSED 

test_delete_from_favorites
# проверяем удаление книги из избранного
# создаем экземпляр (объект) класса BooksCollector
# добавляем одну книгу
# добавляем книгу в избранное
# удаляем книгу из избранного
# проверяем список избранного - он пуст
# PASSED 




