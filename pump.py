from abc import ABC, abstractmethod


# Абстрактный класс для представления насоса
class Pump(ABC):
    def __init__(self, h, k):
        self.h = h
        self.k = k

    @abstractmethod
    def calculate(self):
        pass


# Класс для насоса типа C
class PumpC(Pump):
    def calculate(self):
        print(f"nas_cH рассчитан {self.h * 1}")
        print(f"nas_cK рассчитан {self.k * 2}")
        return self.h * 1 * self.k * 2


# Класс для насоса типа R
class PumpR(Pump):
    def calculate(self):
        print(f"nas_rH рассчитан {self.h * 4}")
        print(f"nas_rK рассчитан {self.k * 8}")
        return self.h * 4 * self.k * 8


# Сборщик насоса по параметрам
class PumpFactory:
    @staticmethod
    def create_pump(type, h, k):
        if type == "C":
            return PumpC(h, k)
        elif type == "R":
            return PumpR(h, k)
        else:
            raise ValueError("Неподдерживаемый тип насоса")


def main():
    # Создание насоса типа C с параметрами H = 2.0, K = 3.0
    pumpC = PumpFactory.create_pump("C", 2.0, 3.0)
    print("Создан насос типа C с параметрами H = 2.0, K = 3.0")
    resultC = pumpC.calculate()
    print("Результат для насоса типа C:", resultC)

    # Создание насоса типа R с параметрами H = 2.0, K = 3.0
    pumpR = PumpFactory.create_pump("R", 2.0, 3.0)
    print("Создан насос типа R с параметрами H = 2.0, K = 3.0")
    resultR = pumpR.calculate()
    print("Результат для насоса типа R:", resultR)


if __name__ == "__main__":
    main()
