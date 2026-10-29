def ft_count_harvest_recursive(harvest_day=None, day=1):
    if harvest_day is None:
        harvest_day = int(input("Days until harvest: "))

    if day > harvest_day:
        print("Harvest time!")
        return

    print(f"Day {day}")
    ft_count_harvest_recursive(harvest_day, day + 1)
