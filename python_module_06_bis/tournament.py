from ex3.factories import CreatureFactory
from ex4.strategy import BattleStrategy, InvalidStrategyError
from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import NormalStrategy, AggressiveStrategy


def battle(opponents: list[tuple[CreatureFactory,
                                 BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory1, strategy1 = opponents[i]
                factory2, strategy2 = opponents[j]

                creature1 = factory1.create_base()
                creature2 = factory2.create_base()

                print("* Battle *")
                print(creature1.describe())
                print("vs.")
                print(creature2.describe())
                print("now fight!")
                strategy1.act(creature1)
                strategy2.act(creature2)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    print("Tournament 0 (basic)")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    battle(opponents)

    print("Tournament 1 (error)")
    opponents = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy())
    ]
    battle(opponents)


if __name__ == "__main__":
    main()
