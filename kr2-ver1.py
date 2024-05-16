from typing import Optional, Union


class PumpParameters:
    def __init__(self, *, Q: Optional[float] = None, H: Optional[float] = None, ro: Optional[float] = None,
                 kpd: Optional[float] = None) -> None:

        self.g: float = 9.81
        self.Q: Optional[float] = Q
        self.H: Optional[float] = H
        self.ro: Optional[float] = ro
        self.kpd: Optional[float] = kpd
        self.check_kpd()

    def check_kpd(self) -> None:
        if self.kpd is not None and not 0 <= self.kpd <= 1:
            print("нереальный КПД")
            self.kpd = None

    def calculate_N(self) -> Union[str, float]:
        if self.kpd is None:
            return self.Np()
        else:
            return self.Nn()

    def Nn(self) -> Union[str, float]:
        if None in (self.Q, self.H, self.ro, self.kpd):
            return "Недостаточно данных для вычисления мощности насоса"
        if self.kpd is None:
            return "Кпд насоса не определен"
        return (self.ro * self.g * self.Q * self.H) / (1000 * self.kpd)

    def Np(self) -> Union[str, float]:
        if None in (self.Q, self.H, self.ro):
            return "Недостаточно данных для вычисления полезной мощности насоса"
        return (self.ro * self.g * self.Q * self.H) / 1000


test1 = PumpParameters(Q=15, H=15, ro=6)
print("Полезная мощность насоса:", test1.calculate_N())

test2 = PumpParameters(Q=15, H=15, ro=6, kpd=0.5)
print("Мощность насоса:", test2.calculate_N())
