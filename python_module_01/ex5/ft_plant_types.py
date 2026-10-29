#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._is_blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._produce_shade = False

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")

    def get_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(
              f"Tree {self._name} now produces a shade of {self._height}cm"
              f"long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 1


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n")
    print("=== Tree")
    oak.show()
    print(f"[asking the {oak.get_name()} to produce shade]")
    oak.produce_shade()
    print("\n")
    print("=== Vegetable")
    tomato.show()
    days = 20
    print(f"[make {tomato.get_name()} grow and age for {days} days]")
    for day in range(days):
        tomato.age()
        tomato.grow()
    tomato.show()
