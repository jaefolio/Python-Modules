

import importlib


def check_library(name: str) -> bool:
    try:
        library = importlib.import_module(name)
    except ImportError as error:
        print(f"[ERROR] Could no load {name}: {error}")
        return False
    print(f"[OK] {name} {library.__version__}")
    return True


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:\n")
    all_available = True
    for name in ("numpy", "pandas"):
        if not check_library(name):
            all_available = False
    if not all_available:
        print("\nInstall the required libraries from the ex0 directory:")
        print("Using pip, with your virtual environment activated:")
        print("  python -m pip install -r requirements.txt")
        print("\nUsing Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
    else:
        print("\npip vs Poetry:\n"
              "requirements.txt declares what to install;"
              "pip resolves it at install time.\n"
              "pyproject.toml declares the same constraints,"
              "and Poetry pins the resolved\n"
              "versions in poetry.lock so every install is identical.\n")
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
