#!/usr/bin/env python3

import sys


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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
        print(f"File '{filename}' closed.\n")
    except (OSError, UnicodeError) as error:
        print(f"Error opening file '{filename}': {error}")
        return

    print("Transform data:")
    print("---\n")

    new_content: str = ""
    lines = content.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    for line in lines:
        new_content += line + "#\n"

    save_name: str = ""
    try:
        print(new_content, end="")
        print("\n---")

        save_name = input("Enter new file name (or empty):")

        if save_name:
            print(f"Saving data to '{save_name}'")
            destination = open(save_name, "w", encoding="utf-8")
            try:
                destination.write(new_content)
            finally:
                destination.close()
            print(f"Data saved in file '{save_name}'.")
        else:
            print("Not saving data.")
    except (OSError, UnicodeError, EOFError) as error:
        print(f"Error saving file '{save_name}': {error}")
        print("Data not saved.")


if __name__ == "__main__":
    main(sys.argv)
