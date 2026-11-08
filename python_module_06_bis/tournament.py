import ex3
import ex4


def battle(opponents: list[tuple[ex3.CreatureFactory,
                                 ex4.BattleStrategy]]) -> None:
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
    except ex4.InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    print("Tournament 0 (basic)")
    opponents = [
        (ex3.FlameFactory(), ex4.NormalStrategy()),
        (ex3.TransformCreatureFactory(), ex4.AggressiveStrategy())
    ]
    result = []

    for factory, strategy in opponents:
        creature = factory.create_base()

        creature_name = type(creature).__name__
        strategy_name = type(strategy).__name__.removesuffix("Strategy")

        result.append(f"({creature_name}+{strategy_name})")

    print(f"[{', '.join(result)}]")
    battle(opponents)

    print("\nTournament 1 (error)")
    opponents = [
        (ex3.TransformCreatureFactory(), ex4.AggressiveStrategy()),
        (ex3.FlameFactory(), ex4.AggressiveStrategy())
    ]
    result = []

    for factory, strategy in opponents:
        creature = factory.create_base()

        creature_name = type(creature).__name__
        strategy_name = type(strategy).__name__.removesuffix("Strategy")

        result.append(f"({creature_name}+{strategy_name})")

    print(f"[{', '.join(result)}]")
    battle(opponents)


if __name__ == "__main__":
    main()
