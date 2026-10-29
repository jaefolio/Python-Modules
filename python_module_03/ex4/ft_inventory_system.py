#!/usr/bin/env python3

import sys


def main(argv) -> None:
    print("== Inventory System Analysis ==")
    inventory = {}

    for arg in argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = parts
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            quantity = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
            continue
        inventory[key] = quantity

    print("Got inventory:", inventory)
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(list(inventory.keys()))} items: "
          f"{sum(inventory.values())}")

    total = sum(inventory.values())
    for item in inventory:  # noqa: PLC0206
        quantity = inventory[item]
        percentage = round(quantity / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    if inventory:
        items = list(inventory.keys())
        most_item = items[0]
        least_item = items[0]

        for item in inventory:  # noqa: PLC0206
            if inventory[item] > inventory[most_item]:
                most_item = item
            if inventory[item] < inventory[least_item]:
                least_item = item

    print(f"Item most abundant: {most_item} "
          f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} "
          f"with quantity {inventory[least_item]}")

    inventory.update({"Moonlight Greatsword": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main(sys.argv)
