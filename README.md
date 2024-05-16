# Перегрузка конструктора + настройка доступа

## access_rights_example.py
```python
self.arg1 = arg1  # Этот атрибут доступен вне класса
self._arg2 = arg2  # Этот атрибут доступен вне класса, но обозначен как "закрытый", по факту закрытый метод
# ничего не делает, кроме предупреждение в IDE и порицания при его использовании вне класса от разработчиков
self.__arg3 = arg3  # Этот атрибут доступен только внутри класса, обозначен как "защищенный"
```

## override_example.py
```python
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
```
