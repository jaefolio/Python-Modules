#!/usr/bin/env python3

import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    args_list = sys.argv[1:]
    if len(args_list) < 1:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    for arg in args_list:
        try:
            val = int(arg)
            scores += [val]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}\n"
          f"Total players: {len(args_list)}\n"
          f"Total score: {sum(scores)}\n"
          f"Average score: {sum(scores) / len(scores)}\n"
          f"High score: {max(scores)}\n"
          f"Low score: {min(scores)}\n"
          f"Score range: {max(scores) - min(scores)}"
          )


if __name__ == "__main__":
    score_analytics()
