

import elements


def alembic_0() -> str:
    element: str = elements.create_fire()
    return element


if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {alembic_0()}")
