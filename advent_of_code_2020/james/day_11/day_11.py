from pathlib import Path
import numpy as np
from collections import defaultdict
from itertools import product


def find_neighbors(i, j):
    adjacent_indexes = [
        [i, j + 1],  # east
        [i + 1, j + 1],  # southeast
        [i + 1, j],  # south
        [i + 1, j - 1],  # southwest
        [i, j - 1],  # west
        [i - 1, j - 1],  # northwest
        [i - 1, j],  # north
        [i - 1, j + 1],  # northeast
    ]
    return adjacent_indexes


def line_search(i, j, slope, map):
    # print(f"Starting location: {i}, {j}")
    end_search = False
    while end_search == False:
        i += slope[0]
        j += slope[1]
        # print(f"Search location: {i}, {j}")
        if i < 0 or j < 0 or i >= len(map) or j >= len(map[i]):
            return
        elif map[i][j] == ".":
            continue
        elif map[i][j] == "L":
            end_search = True
            return
        elif map[i][j] == "#":
            end_search = True
            return [i, j]
    return


def find_visible(i, j, map):
    visible_indexes = []
    slopes = product([-1, 0, 1], repeat=2)
    for slope in slopes:
        if slope != (0, 0):
            loc = line_search(i, j, slope, map)
            if loc:
                visible_indexes.append(loc)
    return visible_indexes


def assess_map_p2(map):
    map = map.copy()
    change_orders = defaultdict(dict)
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            # print(f"Location: {i}, {j}")
            visible_indexes = find_visible(i, j, map)
            visible_indexes = [i * map.shape[1] + j for i, j in visible_indexes]
            visible_seats = map.flatten()[visible_indexes]
            if char == "L" and list(visible_seats).count("#") == 0:
                change_orders[i][j] = "#"
            if char == "#" and list(visible_seats).count("#") >= 5:
                change_orders[i][j] = "L"
    return fill_seats(map, change_orders)


def assess_map_p1(map):
    map = map.copy()
    change_orders = defaultdict(dict)
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            adjacent_indexes = find_neighbors(i, j)
            adjacent_seats = []
            for index in adjacent_indexes:
                if (
                    index[0] >= 0
                    and index[1] >= 0
                    and index[0] < len(map)
                    and index[1] < len(row)
                ):

                    try:
                        adjacent_seats.append(map[index[0]][index[1]])
                    except IndexError:
                        print(f"IndexError: i:{index[0]} j:{index[1]}")
            if char == "L" and adjacent_seats.count("#") == 0:
                change_orders[i][j] = "#"
            if char == "#" and adjacent_seats.count("#") >= 4:
                change_orders[i][j] = "L"
    return fill_seats(map, change_orders)


def fill_seats(map, change_orders):
    for i in change_orders.keys():
        for j in change_orders[i].keys():
            map[i][j] = change_orders[i][j]
    return map


# def print_map(map):
#     for row in map:
#         print(["".join(char) for char in row.tolist()])


if __name__ == "__main__":
    input_path = Path.cwd() / "day_11" / "input_day_11.txt"
    map_raw = open(input_path).read().split("\n")
    for i, row in enumerate(map_raw):
        map_raw[i] = [char for char in row]

    map = np.array(map_raw)
    stabilized = False
    count = 0
    while not stabilized:
        # new_map = assess_map_p1(map)
        new_map = assess_map_p2(map)
        stabilized = (new_map == map).all()
        map = new_map
        # print_map(map)
        count += 1
        print(f"count: {count}")
    unique, counts = np.unique(map, return_counts=True)
    print(dict(zip(unique, counts)))
