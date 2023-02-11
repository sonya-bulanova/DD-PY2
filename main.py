"Базовый класс частицы"
"У всех частиц есть заряд, масса и спин"
""" Атрибуты сделаны protected, чтобы их напрямую нельзя было изменять вне класса """
""" ДЛя изменения параметров вводятся сеттеры, а для получения параметров -- геттеры """
""" Пример создания объекта: particle = Particle(0.5, 2, 985.) """
class Particle:
    """Инициализация экземпляра класса"""
    def __init__(self, spin: float, charge: int, mass: float):
        self._spin = None
        self.set_spin(spin)
        self._charge = None
        self.set_charge(charge)
        self._mass = None
        self.set_mass(mass)
    """ Спин может быть целым или полуцелым, поэтому при передаче других значений генерируется ошибка 
    Пример использования сеттера: particle.set_spin(2.5) """
    def set_spin(self, new_spin: float) -> None:
        if not isinstance(new_spin, (int, float)):
            raise TypeError
        if new_spin % 0.5 == 0:
            self._spin = new_spin
        else:
            raise ValueError
    """ Проверка значения заряда на то, что это целое число -- 
    пусть заряд выражается в единицах элементарного заряда """
    def set_charge(self, new_charge: int) -> None:
        if not isinstance(new_charge, (int, float)):
            raise TypeError
        self._charge = new_charge
    """ Масса должна быть неотрицательным числом """
    def set_mass(self, new_mass: float) -> None:
        if not isinstance(new_mass, (int, float)):
            raise TypeError
        if new_mass < 0:
            raise ValueError
        else:
            self._mass = new_mass
    """ Геттеры, чтобы получить значения инкапсулированных методов """
    """ Пример использования геттера: particle.get_spin()  """
    def get_spin(self) -> float:
        return self._spin

    def get_charge(self) -> int:
        return self._charge

    def get_mass(self) -> float:
        return self._mass
    """ Реализация магических методов для базового класса """
    """ Пример использования магического метода: particle.__str__() """
    def __str__(self) -> str:
        return f'Частица {self._spin}. Заряд {self._charge}. Масса {self._mass}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(spin={self._spin!r}, charge={self._charge!r}, mass={self._mass!r})"
    """ Метод поиска античастицы, в базовом классе возвращает заряд частицы с противоположным знаком """
    """ Пример использования метода: particle.find_antiparticle() """
    def find_antiparticle(self) -> int:
        return -self._charge
    """ Метод вычисления времени жизни частицы """
    """ Пример использования метода: particle.count_lifetime() """
    def count_lifetime(self) -> float:
        ...

""" Дочерний класс -- мюон. У него, помимо родительских атрибутов, есть два дополнительных -- быстрота и импульс """
""" Атрибуты тоже инкапсулированы, чтобы не произошло неявного изменения вне класса """
""" Пример создания объекта класса Muon: muon = Muon(0.5, 2, 985., 7., 3457.) """
class Muon(Particle):
    def __init__(self, spin: float, charge: int, mass: float, rapidity: float, momentum: float):
        super().__init__(spin, charge, mass)
        self._rapidity = None
        self.set_rapidity(rapidity)
        self._momentum = None
        self.set_momentum(momentum)
    """ Пишем аннотацию типов для методов set_rapidity и set_momentum """
    """ Можно передавать численные значения типов int или float """
    """ Пример использования методов: muon.set_rapidity(6.) """
    def set_rapidity(self, new_rapidity: float) -> None:
        if not isinstance(new_rapidity, (int, float)):
            raise TypeError
        self._rapidity = new_rapidity

    def set_momentum(self, new_momentum: float) -> None:
        if not isinstance(new_momentum, (int, float)):
            raise TypeError
        else:
            self._momentum = new_momentum
    """ Геттеры, чтобы получить значения инкапсулированных методов """
    """ Пример использования геттера: muon.get_rapidity()  """
    def get_rapidity(self) -> float:
        return self._rapidity

    def get_momentum(self) -> float:
        return self._momentum
    """ Перегружаем магические методы __str__ and __repr__, чтобы они возвращали дочерний класс """
    def __str__(self) -> str:
        return f'Частица {self._spin}. Заряд {self._charge}. Масса {self._mass}.' \
               f' Быстрота{self._rapidity}. Импульс{self._momentum}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(spin={self._spin!r}, charge={self._charge!r}, mass={self._mass!r}, " \
               f"rapidity={self._rapidity!r}, momentum={self._momentum!r})"
    """" Новый метод в дочернем классе -- set_trajectory 
    Пример использования метода: muon.set_trajectory()"""
    def set_trajectory(self) -> None:
        ...
    """ Метод, проверяющий, является ли частица релятивистской
     Пример использования: muon.is_relativistic()"""
    def is_relativistic(self) -> bool:
        ...
    """ Метод find_antiparticle наследуется от родительского класса """
    def find_antiparticle(self) -> int:
        super().find_antiparticle(self)
    """ Вычисление времени жизни зависит от того, является ли частица релятивистской.
     Если частица нерелятивистская, тогда метод должен работать также, как в родительском классе.
     Если частица релятивистская, тогда нужно будет учитывать релятивистское увеличение времени жизни
     Пример использования: muon.count_lifetime()"""
    def count_lifetime(self) -> float:
        if self.is_relativistic:
            ...
        else:
            super().count_lifetime(self)
