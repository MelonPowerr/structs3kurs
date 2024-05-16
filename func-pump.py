from typing import Callable, Optional, Union


def check_kpd(kpd: Optional[float]) -> Optional[float]:
    if kpd is not None and not 0 <= kpd <= 1:
        print("нереальный КПД")
        return None
    return kpd


def calculate_N(func1: Callable, func2: Callable) -> Callable:
    def allocate(*, Q: Optional[float] = None, H: Optional[float] = None, ro: Optional[float] = None,
                 kpd: Optional[float] = None) -> Union[str, float]:
        g: float = 9.81

        kpd = check_kpd(kpd)

        if kpd is None:
            return func1(Q, H, ro, g)
        else:
            return func2(Q, H, ro, g, kpd)

    return allocate


def Nn(Q: Optional[float], H: Optional[float], ro: Optional[float], g: Optional[float],
       kpd: Optional[float]) -> Union[str, float]:
    if None in (Q, H, ro, kpd):
        return "Недостаточно данных для вычисления мощности насоса"
    return (ro * g * Q * H) / (1000 * kpd)


def Np(Q: Optional[float], H: Optional[float], ro: Optional[float], g: Optional[float]) -> Union[str, float]:
    if None in (Q, H, ro):
        return "Недостаточно данных для вычисления полезной мощности насоса"
    return (ro * g * Q * H) / 1000


test1 = calculate_N(Np, Nn)(Q=15, H=15, ro=6)
print(f"Полезная мощность насоса: {test1}")

test2 = calculate_N(Np, Nn)(Q=15, H=15, ro=6, kpd=0.5)
print(f"Мощность насоса: {test2}")
