from pathlib import Path
import math


def to_matrix(map):
    for idx, line in enumerate(map):
        map[idx] = [char for char in line]
    return map


def extend_map(map, max_slope):
    # this extends the map enough to reach the bottom without running out of space
    needed_extensions = math.ceil(len(map) * max_slope / len(map[0]))  # + 1
    for idx, line in enumerate(map):
        map[idx] = line * needed_extensions
    return map


def slide_step(point, down, right):
    point[0] += down
    point[1] += right
    return point


def traverse_map(map, slope=(1, 3)):
    tree_count = 0
    location = [0, 0]
    for _ in range(len(map)):
        location = slide_step(location, down=slope[0], right=slope[1])
        row = location[0]
        col = location[1]
        try:
            landing = map[row][col]
        except IndexError as e:
            print(f"Problem landing on location: {row}, {col}")
        if landing == "#":
            # print("Landed on tree")
            tree_count += 1
        if row == len(map) - 1:
            print(f"Final location: {row}, {col}")
            return tree_count


if __name__ == "__main__":
    input_path = Path.cwd() / "day_3" / "input_day_3.txt"
    map_raw = open(input_path).read().splitlines()
    max_slope = 7

    map_matrix = to_matrix(map_raw)
    map_long = extend_map(map_matrix, max_slope)
    print("Part I")
    tree_count = traverse_map(map_long)
    print(f"Final tree count: {tree_count} \n")

    print("Part II")
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    product = 1
    for slope in slopes:
        tree_count = traverse_map(map_long, slope)
        product *= tree_count
        print(product)
