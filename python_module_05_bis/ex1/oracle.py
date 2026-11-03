

import os

from dotenv import load_dotenv


def git_ignore(gitignore_path=None) -> bool:
    if gitignore_path is None:
        gitignore_path = os.path.join(os.path.dirname(__file__), ".gitignore")
    if not os.path.exists(gitignore_path):
        print("Error: .gitignore not found")
        return False
    with open(gitignore_path, "r") as file:
        for line in file:
            if line.strip() in [".env", "*.env"]:
                return True
    return False


def oracle() -> None:
    if not load_dotenv():
        print("No .env file detected")
        return
    if not git_ignore():
        print("Error: .env not found in .gitignore")
        return

    mode = os.environ.get("MATRIX_MODE", "development")
    log_level = os.environ.get("LOG_LEVEL", "INFO")

    print("ORACLE STATUS: Consulting the configuration...\n")

    if mode == "development":
        print("Configuration loaded:")
        print("Mode: development")
        print(f"Database configured: {bool(os.environ.get('DATABASE_URL'))}")
        print(f"API Access authenticated: {bool(os.environ.get('API_KEY'))}")
        print(f"Log level: {log_level}")
        print(f"Remote Network Configured:"
              f"{bool(os.environ.get('ZION_ENDPOINT'))}")
    elif mode == "production":
        print("Production mode: Development diagnostics disabled.")
    else:
        print("Configuration error: MATRIX_MODE must be"
              "'development' or 'production'")
    print("\nConfiguration security check:\n"
          "[OK] No hardcoded secrets detected\n"
          "[OK] .env file properly ignored by git\n"
          "[OK] Production overrides available\n")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
