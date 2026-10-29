#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    if int(temp_str) < 0:
        raise ValueError(f"{temp_str}°C is too"
                         f" cold for plants (min 0°C)")
    elif int(temp_str) > 40:
        raise ValueError(f"{temp_str}°C is too"
                         f" hot for plants (max 40°C)")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print(" ")
    for value in ("25", "abc", "100", "-50"):
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
