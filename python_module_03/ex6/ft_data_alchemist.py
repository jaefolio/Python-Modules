#!/usr/bin/env python3

import random


def main() -> None:
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']

    print("== Game Data Alchemist")
    print("Initial list of players:", players)

    cap_players = [player.capitalize() for player in players]
    print("New list with all names capitalized:", cap_players)

    cap_only = [player for player in players if 'A' <= player[0] <= 'Z']
    print("New list of capitalized names only:", cap_only)

    scores = {player: random.randint(0, 1000) for player in cap_players}
    print("Score dict:", scores)

    average = sum(scores.values()) / len(scores.values())
    print(f"Score average is {round(average, 2)}")

    high_scores = {player: scores[player]
                   for player in scores if scores[player] > average}
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
