#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for name in ("Tomato", "Lettuce", "Carrots"):
            water_plant(name)
    except PlantError as error:
        print(f"Caught Plant Error: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system \n")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for name in ("Tomato", "lettuce", "Carrots"):
            water_plant(name)
    except PlantError as error:
        print(f"Caught Plant Error: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system \n")


if __name__ == "__main__":
    print("=== Garden Watering System === \n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
