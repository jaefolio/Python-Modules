#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._height = 0.0
        else:
            self._age = age

    def show(self) -> None:
        print(f"Created: {self._name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height} cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}:Error, age can't be negative")
            print("Age update rejected")


if __name__ == "__main__":
    plant1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    plant1.show()
    print("\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-25)
    plant1.set_age(-30)
    print("\n")
    print(
        f"Current state: {plant1._name}: "
        f"{plant1.get_height():.1f}cm, "
        f"{plant1.get_age()} days old"
    )
