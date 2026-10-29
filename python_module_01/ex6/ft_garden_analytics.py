#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def age(self, days: int) -> None:
        self._stats.record_age()
        self._age += days

    def grow(self, cm: float) -> None:
        self._stats.record_grow()
        self._height += cm

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def check_age(age: int) -> None:
        if age <= 365:
            print(f"Is {age} days more than a year? -> False")
        else:
            print(f"Is {age} days more than a year? -> True")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown Plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display_calls(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def display_calls(self) -> None:
        self._stats.display_calls()


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

    def add_height(self, cm: float) -> None:
        super().grow(cm)


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds : {round(self._seeds)}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._produce_shade = False
        self.shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")

    def get_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(
              f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")

    def record_shade(self) -> None:
        self.shade_calls += 1

    def display_calls(self) -> None:
        super().display_calls()
        print(f"{self.shade_calls} shade")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_calls()


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    anonymous = Plant.create_anonymous()

    print("=== Garden Statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n")

    print("=== Flower")
    rose.show()
    print(f"[asking the {rose.get_name()} to grow and bloom]")
    display_statistics(rose)
    rose.add_height(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print("\n")

    print("=== Tree")
    oak.show()
    display_statistics(oak)
    print(f"[asking the {oak.get_name()} to produce shade]")
    oak.produce_shade()
    oak.record_shade()
    display_statistics(oak)
    print("\n")

    print("=== Seed")
    sunflower.show()
    print(f"[make {sunflower.get_name()} grow, age and bloom]")
    sunflower.bloom()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print("\n")

    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)
