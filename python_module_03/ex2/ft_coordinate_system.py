#!/usr/bin/env python3

import math


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Gets a first set of coordinates")
    coord_1: tuple = get_player_pos()
    center_dist = math.sqrt((coord_1[0]-0.0)**2 + (coord_1[1]-0.0)**2
                            + (coord_1[2]-0.0)**2)
    print(f"Got a first tuple: {coord_1}\n"
          f"It includes: X={coord_1[0]}, Y={coord_1[1]}, "
          f"Z={coord_1[2]}\n"
          f"Distance to center: {round(center_dist, 4)}\n"
          )
    print("Gets a second set of coordinates")
    coord_2: tuple = get_player_pos()
    dist = math.sqrt((coord_1[0]-coord_2[0])**2 + (coord_1[1]-coord_2[1])**2
                     + (coord_1[2]-coord_2[2])**2)
    print(f"Got a first tuple: {coord_2}\n"
          f"It includes: X={coord_2[0]}, Y={coord_2[1]}, "
          f"Z={coord_2[2]}\n"
          f"Distance to center: {round(dist, 4)}\n"
          )


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as "
                           "floats in format 'x,y,z':")
        pos_tuple = tuple(user_input.split(","))
        try:
            x, y, z = pos_tuple
        except ValueError:
            print("Invalid syntax")
            continue

        values = []
        try:
            for value in (x, y, z):
                values += [float(value)]
        except ValueError as error:
            print(f"Error on parameter {error}: "
                  f"could not convert string to float: {error}")
            continue
        return tuple(values)


if __name__ == "__main__":
    main()
