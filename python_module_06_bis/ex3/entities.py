from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, entity_name: str, entity_type: str) -> None:
        self._name = entity_name
        self._type = entity_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self._name} is a {self._type} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if not self._transformed:
            return ("Shiftling attacks normally.")
        else:
            return ("Shiftling performs a boosted strike!")

    def transform(self) -> str:
        self._transformed = True
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        self._transformed = False
        return ("Shiftling returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if not self._transformed:
            return ("Morphagon attacks normally.")
        else:
            return ("Morphagon unleashes a devastating morph strike!")

    def transform(self) -> str:
        self._transformed = True
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        self._transformed = False
        return ("Morphagon stabilizes its form.")
