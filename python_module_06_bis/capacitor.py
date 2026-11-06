from ex3 import TransformCreatureFactory


def main():
    trans = TransformCreatureFactory()
    t_creature = trans.create_base()
    t_evolved = trans.create_evolved()
    print("Transform creature with transform capability")
    print("base:")
    print(t_creature.describe())
    print(t_creature.attack())
    print(t_creature.transform())
    print(t_creature.attack())
    print(t_creature.revert())
    print("evolved:")
    print(t_evolved.describe())
    print(t_evolved.attack())
    print(t_evolved.transform())
    print(t_evolved.attack())
    print(t_evolved.revert())


if __name__ == "__main__":
    main()
