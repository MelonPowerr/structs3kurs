class MyClass:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1  # Этот атрибут доступен вне класса
        self._arg2 = arg2  # Этот атрибут доступен вне класса, но обозначен как "закрытый", по факту закрытый метод
        # ничего не делает, кроме предупреждение в IDE и порицания при его использовании вне класса от разработчиков
        self.__arg3 = arg3  # Этот атрибут доступен только внутри класса, обозначен как "защищенный"

    def show_args(self):
        print(self.arg1, self._arg2, self.__arg3)


def main():
    obj = MyClass(1, 2, 3)
    print(obj.arg1)
    print(obj._arg2)
    # print(obj.__arg3)  # тут будет ошибка, ибо аттрибут защищен

    obj.arg1 = 3
    obj._arg2 = 1
    obj.__arg3 = 2
    obj.show_args()  # аргументы 1 и 2 изменили значения, третий остался без изменений


if __name__ == "__main__":
    main()
