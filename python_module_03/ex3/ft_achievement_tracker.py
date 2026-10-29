#!/usr/bin/env python3

import random


def gen_player_achievements() -> None:
    achievements = {
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'Hidden Path Finder',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer'
    }
    alice = set()
    bob = set()
    charlie = set()
    dylan = set()

    a = random.randint(1, len(achievements))
    b = random.randint(1, len(achievements))
    c = random.randint(1, len(achievements))
    d = random.randint(1, len(achievements))

    alice.update(random.sample(list(achievements), a))
    bob.update(random.sample(list(achievements), b))
    charlie.update(random.sample(list(achievements), c))
    dylan.update(random.sample(list(achievements), d))
    print("=== Achievement Tracker System ===\n")
    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("\n")

    union = alice.union(bob, charlie, dylan)
    intersection = alice.intersection(bob, charlie, dylan)

    print("All distinct achievements:", union)
    print("\n")
    print("Common achievements:", intersection)
    print("\n")

    print("Only Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(alice, charlie, dylan))
    print("Only Charlie has:", charlie.difference(bob, alice, dylan))
    print("Only Dylan has:", dylan.difference(bob, charlie, alice))
    print("\n")

    print("Alice is missing:", achievements.difference(alice))
    print("Bob is missing:", achievements.difference(bob))
    print("Charlie is missing:", achievements.difference(charlie))
    print("Dylan is missing:", achievements.difference(dylan))


if __name__ == "__main__":
    gen_player_achievements()
