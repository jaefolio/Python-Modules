from abc import ABC, abstractmethod
from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import NormalStrategy, AggresiveStrategy


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggresive = AggresiveStrategy()

    opponents: tuple[CreatureFactory, BattleFactory]
