#!/usr/bin/env python3

import sys


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': "
                         f"{error}\n")
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
        print("Enter new file name (or empty):", end="", flush=True)
        save_name = sys.stdin.readline()
        if save_name[-1:] == "\n":
            save_name = save_name[:-1]

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
    except (OSError, UnicodeError) as error:
        sys.stderr.write(f"[STDERR] Error opening file '{save_name}': "
                         f"{error}\n")
        print("Data not saved.")


if __name__ == "__main__":
    main(sys.argv)
