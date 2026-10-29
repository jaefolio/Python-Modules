#!/usr/bin/env python3


def garden_operations(operation_number: int) -> int | float | None:
    if operation_number == 0:
        return int("abc")
    elif operation_number == 1:
        result = 10 / 0
        return result
    elif operation_number == 2:
        with open("/non/existent/file", "r") as file:
            print(file)
    elif operation_number == 3:
        age = 25
        print("I am " + age)
    return None


def test_error_types() -> None:
    for number in (0, 1, 2, 3, 4):
        print(f"Testing operation {number}...")
        try:
            garden_operations(number)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
    print(" ")
    print("All error types tested successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
