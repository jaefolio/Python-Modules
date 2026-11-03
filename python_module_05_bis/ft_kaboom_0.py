from alchemy.grimoire.light_spellbook import light_spell_record


def kaboom_0() -> str:
    return light_spell_record("Phoenix Rebirth",
                              "dragon's cum, phoenix ash, ruby dust")


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(kaboom_0())
