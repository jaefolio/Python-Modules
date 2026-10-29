#!/usr/bin/env python3

import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    index = 1
    for arg in sys.argv[1:]:
        print(f"Argument {index}: {arg}")
        index += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
