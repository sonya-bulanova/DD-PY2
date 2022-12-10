# TODO Написать 3 класса с документацией и аннотацией типов
from math import log, floor


class GameEnemy:
    """
    Класс описывает модель врага в игре
    Пример создания объекта класса:
    enemy = GameEnemy("daemon", "I'll burn you!", 400)
    """
    def __init__(self, name: str, phrase: str, force: int):
        """Инициализация экземпляра класса"""
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        if not isinstance(phrase, str):
            raise TypeError
        self.phrase = phrase

        """Сила врага всегда целочисленна и положительна"""
        if not isinstance(force, int):
            raise TypeError
        if force < 0:
            raise ValueError
        self.force = force

    def say_phrase(self) -> None:
        """Враг хвастается перед игроком
        enemy.say_phrase()
        Выводится фраза "I'll burn you!"
        """
        ...

    def increase_force(self, extra_force: int) -> int:
        """Враг может увеличить свою силу
        К переменной force прибавляется extra_force и
        возвращается новое значение силы

        пример: enemy.increase_force(150)
        """
        ...


class Planet:
    """
    Класс описывает планету, имеющую название, ускорение свободного падения и обитаемую/необитаемую
    Пример: planet = Planet("Glisse 576", False, 9.78)
    """
    def __init__(self, name: str, habitation: bool, gravity: float):
        self.name = name
        """Обитаемость -- логическое выражение, т.е. планета может быть или обитаемой, или необитаемой"""
        if not isinstance(habitation, bool):
            raise TypeError
        self.habitation = habitation

        """Ускорение свободного падения не может быть отрицательным и должно быть числом --
        целым или с плавающей точкой
        """
        if not isinstance(gravity, (float, int)):
            raise TypeError
        if gravity < 0:
            raise ValueError
        self.gravity = gravity

    def populate_planet(self, population: int) -> int:
        """Можно колонизировать планету, передать количество жителей, тогда habitation станет true
        Вернется значение нового населения планеты
        Пример: planet.populate_planet(100)
        """
        ...

    def calc_planet_mass(self) -> float:
        """Можно рассчитать массу планеты через ускорение свободного падения и вернуть значение массы
        Пример: mass = planet.calc_planet_mass()
        """
        ...

    def change_name(self, new_name: str) -> str:
        """ Можно переименовать планету, передать в метод новое имя
        Необходимо проверить, является ли имя строкой
        Вернется новое название планеты
        Пример: mass.change_name("Mars")
        """
        ...


class Laptop:
    """
    Класс ноутбуков. У ноутбука есть название модели (model),
    вес (weight), оперативная память (ram) и модель процессора (processor_model)
    Пример вызова:
    acer_nitro = Laptop("Acer Nitro 5 AN-517", 2.78, 16, "Ryzen 5")
    """
    def __int__(self, model: str, weight: float, ram: int, processor_model: str):
        if not isinstance(model, str):
            raise TypeError
        self.model = model

        """Вес должен быть числом с точностью до десятых"""
        if not isinstance(weight, float):
            raise TypeError
        if weight < 0:
            raise ValueError
        self.weight = weight

        """
        Оперативная память должна быть целой, положительной и являться степенью двойки -- 
        не может быть 3, 5 Гб или 10.5 Гб
        """
        if not isinstance(ram, int):
            raise TypeError
        if ram < 0 and floor(log(ram) / log(2)) is False:
            raise ValueError
        self.ram = ram
        self.processor_model = processor_model

    def show_characteristics(self) -> None:
        """Можно вывести характеристики ноутбука,
        метод не возвращает ничего, но выводит характеристики
        по запросу пользователя

        Пример: acer_nitro.show_characteristics()
        """
        ...

    def increase_ram(self, extra_ram) -> int:
        """Можно добавить оперативной памяти --
        дополнительная память (extra_ram) должна быть тоже степенью двойки

        Пример: некорректно -- acer_nitro.increase_ram(9)
        корректно -- acer_nitro.increase_ram(16)
        """
        ...

    def change_proc(self, new_proc_model) -> str:
        """Можно проапгрейдить процессор ---
        меняется название его модели, возвращается модель нового процессора

        Пример: acer_nitro.change_proc("Intel core i9")
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
