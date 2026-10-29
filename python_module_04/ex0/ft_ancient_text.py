#!/usr/bin/env python3

import sys


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        try:
            content = file.read()
        finally:
            file.close()
        print("---\n")
        print(content, end="" if content.endswith("\n") else "\n")
        print("\n---")
        print(f"File '{filename}' closed.")
    except (OSError, UnicodeError) as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    main(sys.argv)
