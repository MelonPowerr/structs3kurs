class Kettle:
    def __init__(self, water_level=0, is_on_fire=False, is_water_boiling=False, max_water_level=1000):
        self.water_level = water_level
        self.is_on_fire = is_on_fire
        self.is_water_boiling = is_water_boiling
        self.max_water_level = max_water_level

    def fill_kettle(self):
        if self.water_level == 0:
            self.water_level = self.max_water_level
            print(f"Чайник наполнен водой. Текущий уровень воды: {self.water_level} мл")
        else:
            self.add_water()

    def add_water(self):
        amount = self.max_water_level - self.water_level
        self.water_level += amount
        print(f"Добавлено {amount} мл воды в чайник. Текущий уровень воды: {self.water_level} мл")

    def turn_on_fire(self):
        if self.water_level == 0:
            raise ValueError("Невозможно включить огонь. Сначала добавьте воду.")
        self.is_on_fire = True
        print("Огонь поджёгся под чайником")

    def wait_for_boiling(self):
        if self.is_on_fire and self.water_level > 0:
            print("Ожидаем кипения воды...")
            self.is_water_boiling = True
            print("Вода закипает!")
        else:
            print("Невозможно вскипятить воду. Проверьте, что чайник на огне и содержит воду.")


def boiling_water_in_kettle(kettle):
    kettle.fill_kettle()
    kettle.turn_on_fire()
    kettle.wait_for_boiling()


def main():
    kettle1 = Kettle(0)
    kettle2 = Kettle(500)
    kettle3 = Kettle(1000)

    print(f"Уровень воды: {kettle1.water_level} мл")
    boiling_water_in_kettle(kettle1)

    print(f"Уровень воды: {kettle2.water_level} мл")
    boiling_water_in_kettle(kettle2)

    print(f"Уровень воды: {kettle3.water_level} мл")
    boiling_water_in_kettle(kettle3)


if __name__ == "__main__":
    main()
