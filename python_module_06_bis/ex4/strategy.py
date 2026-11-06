from abc import ABC, abstractmethod
from ex3.entities import Creature, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        pass


class InvalidStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, Creature)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError("Invalid Creature")
        print(entity.attack())


class AggresiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            raise InvalidStrategyError("Invalid Creature"
                                       f"'{type(entity).__name__}'"
                                       "for this aggresive strategy")

        print(entity.attack())
