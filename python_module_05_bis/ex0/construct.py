#!/usr/bin/env python3


import os
import site
import sys


def detect_environment() -> str:
    if getattr(sys, "base_prefix", sys.prefix) != sys.prefix:
        return "sealed"
    return "unsealed"


if __name__ == "__main__":
    environment: str = detect_environment()
    if environment == "unsealed":
        print(
            "LABORATORY STATUS: You are working in the open\n\n"
            f"Current Python: {sys.executable}\n"
            "Virtual Environment: None detected \n\n"
            "WARNING: You are in the global environment!\n"
            "Every reagent you install here leaks into the whole system.\n\n"
            "To seal the laboratory, run:\n"
            "python3 -m venv lab_env\n"
            "source lab_env/bin/activate # On Unix\n"
            "lab_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    elif environment == "sealed":
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)
        print(
            "LABORATORY STATUS: The laboratory is sealed\n\n"
            f"Current Python: {sys.executable}\n"
            f"Virtual Environment: {venv_name} \n"
            f"Environment Path: {venv_path}\n\n"
            "SUCCESS: You are working in an isolated environment!\n"
            "Safe to install reagents without affecting\n"
            "the global system.\n\n"
            "Reagent installation path:\n"
            f"{site.getsitepackages()[0]}"
        )
