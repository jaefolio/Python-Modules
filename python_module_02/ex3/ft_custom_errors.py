#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(message)


def test_error_types() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught Plant Error: {error}")
    print(" ")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught Water Error: {error}")
    print(" ")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught Garden Error: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught Garden Error: {error}")
    print(" ")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print(" ")
    test_error_types()
