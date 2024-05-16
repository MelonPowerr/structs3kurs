class MathOperations:
    """
    В питоне нет такого понятия как перегрузка конструктора
    Поэтому принято подставлять дефолтные None к аргументам
    И ставить условия выполнения
    """
    def __init__(self, a, b=None, c=None):
        if b is not None and c is not None:
            self.result = a + b + c
        elif b is not None:
            self.result = a + b
        else:
            self.result = a


class MathOperations2:
    """
    Можно еще сделать так, но за перегрузку это не считается
    И работает только если у нас особо нет логики
    Как тут используется sum
    """
    def __init__(self, *args):
        self.result = sum(args)


def main():
    math_obj1 = MathOperations(5)
    math_obj2 = MathOperations(5, 10)
    math_obj3 = MathOperations(5, 10, 15)

    print(math_obj1.result)  # Вывод: 5
    print(math_obj2.result)  # Вывод: 15
    print(math_obj3.result)  # Вывод: 30

    print("##################")

    math_obj1 = MathOperations2(5)
    math_obj2 = MathOperations2(5, 10)
    math_obj3 = MathOperations2(5, 10, 15)

    print(math_obj1.result)  # Вывод: 5
    print(math_obj2.result)  # Вывод: 15
    print(math_obj3.result)  # Вывод: 30


if __name__ == "__main__":
    main()
