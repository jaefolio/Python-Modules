from alchemy.grimoire.dark_spellbook import dark_spell_record


def kaboom_1() -> str:
    return dark_spell_record("Phoenix Rebirth",
                             "FIRE, phoenix ash, ruby dust")


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly"
          "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(kaboom_1())
