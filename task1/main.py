class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = None
        self.set_name(name)
        self.__author = None
        self.set_author(author)

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def set_author(self, new_author: str) -> None:
        self.__author = new_author

    def __str__(self) -> str:
        return f'Книга {self.__name}. Автор {self.__author}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__pages = None
        self.set_pages(pages)

    def set_pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.__pages = new_pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__duration = None
        self.set_duration(duration)

    def set_duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Длительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self.__duration = new_duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r})"


# print(Book("Погребенный с фараонами", "Лавкрафт"))
# print(PaperBook("Цусима", "Новиков-Прибой", 789))
# print(AudioBook("Гиперион", "Dan Simmons", 5.06))