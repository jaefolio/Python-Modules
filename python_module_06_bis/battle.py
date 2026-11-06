from ex3 import FlameFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Factory")
    flame = FlameFactory()
    creature = flame.create_base()
    evolved = flame.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")

    print("Testing Factory")
    trans = TransformCreatureFactory()
    t_creature = trans.create_base()
    t_evolved = trans.create_evolved()
    print(t_creature.describe())
    print(t_creature.attack())
    print(t_evolved.describe())
    print(t_evolved.attack())
    print("")

    print("Testing battle")
    print(creature.describe())
    print("vs.")
    print(t_creature.describe())
    print("fight!")
    print(creature.attack())
    print(t_creature.attack())


if __name__ == "__main__":
    main()
