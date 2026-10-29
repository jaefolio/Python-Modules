#!/usr/bin/env python3


def secure_archive(filename: str, action: str, content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                condition: tuple[bool, str] = True, content
        elif action == "write":
            if content:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(content)
                    condition = True, content
            else:
                raise OSError("Please enter a message")
        else:
            condition = False, f"Unknown action: {action}"
    except OSError as error:
        error_condition: tuple[bool, str] = False, str(error)
        return error_condition
    return condition


def vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    success, message = secure_archive("/not/existing/file", "read")
    print((success, message))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    success, message = secure_archive("test.txt", "read")
    print((success, message))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    success, message = secure_archive("ancient_fragment.txt", "read")
    print((success, message))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    success, message = secure_archive(
        "a.txt", "write", "Content successfully written to file"
    )
    print((success, message))
    print()

    print("Using 'secure_archive' to write to a regular file but no message:")
    success, message = secure_archive("a.txt", "write")
    print((success, message))
    print()

    print("Using 'secure_archive' to test invalid action:")
    success, message = secure_archive("a.txt", "search")
    print((success, message))
    print()


if __name__ == "__main__":
    vault_security()
