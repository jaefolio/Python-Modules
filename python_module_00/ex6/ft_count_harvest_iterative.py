
def ft_count_harvest_iterative():
    harvest_days = input("Days until harvest: ")
    for i in range(1, int(harvest_days) + 1, 1):
        print(f"Day {i}")
    print("Harvest time!")
