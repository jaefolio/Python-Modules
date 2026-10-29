#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print(" ")
    for value in ("25", "abc"):
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}℃")
            print(" ")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
            print(" ")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
