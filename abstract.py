from abc import ABC, abstractmethod


class AKPD(ABC):
    __g: float = 9.81

    @staticmethod
    def set_gravity(value: float):
        AKPD.__g = value

    @staticmethod
    def get_gravity() -> float:
        return AKPD.__g

    @abstractmethod
    def calculate(self) -> float:
        pass


class Nn(AKPD):
    def __init__(self, *, Q: float, H: float, ro: float, kpd: float) -> None:
        self.Q: float = Q
        self.H: float = H
        self.ro: float = ro
        self.kpd: float = kpd

    def calculate(self) -> float:
        return (self.ro * AKPD.get_gravity() * self.Q * self.H) / (1000 * self.kpd)


class Np(AKPD):
    def __init__(self, *, Q: float, H: float, ro: float) -> None:
        self.Q: float = Q
        self.H: float = H
        self.ro: float = ro

    def calculate(self) -> float:
        return (self.ro * AKPD.get_gravity() * self.Q * self.H) / 1000


def main():
    AKPD.set_gravity(9.81)

    PolezniyPower = Np(Q=15, H=15, ro=6)
    print(PolezniyPower.calculate())

    Power = Nn(Q=15, H=15, ro=6, kpd=0.5)
    print(Power.calculate())


if __name__ == "__main__":
    main()