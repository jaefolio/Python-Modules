#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, start_age: int) -> None:
        self.name = name
        self.height = height
        self.start_age = start_age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.start_age} "
              "days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.start_age += 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    starting_height = plant1.height
    print("=== Garden PLant Growth ===")
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print(f"Growth this week: {round(plant1.height - starting_height, 1)}cm")
