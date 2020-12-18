from pathlib import Path
import math


def rotate(origin, point, angle):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (round(qx), round(qy))


def move(go, loc, amount, moves_dict):
    print(f"go: {go}, {amount}")
    dir = [i * amount for i in moves_dict[go]]
    loc = [loc[0] + dir[0], loc[1] + dir[1]]
    return loc


def turn(origin, turn, vector, amount, moves_dict):
    if turn == "R":
        vector = rotate(origin, vector, amount)
    if turn == "L":
        vector = rotate(origin, vector, -amount)
    return vector


def read_moves_p1(moves):
    loc = [0, 0]
    moves_dict = {"E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1)}
    facing = "E"
    for mv in moves:
        go, amount = str(mv[0]), int(mv[1:])
        if go == "F":
            go = facing
        if go in ("N", "E", "S", "W"):
            loc = move(go, loc, amount, moves_dict)
        else:
            facing = turn([0, 0], go, moves_dict[facing], amount, moves_dict)
            facing = [key for key, value in moves_dict.items() if value == facing][0]
    return loc


def approach_waypoint(loc, waypoint, amount):
    vector = [(x - y) * amount for x, y in zip(waypoint, loc)]
    loc = [loc[i] + vector[i] for i in range(2)]
    waypoint = [waypoint[i] + vector[i] for i in range(2)]
    return loc, waypoint


def read_moves_p2(moves):
    loc = [0, 0]
    waypoint = [10, -1]
    moves_dict = {"E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1)}
    for mv in moves:
        go, amount = str(mv[0]), int(mv[1:])
        if go == "F":
            loc, waypoint = approach_waypoint(loc, waypoint, amount)
        elif go in ("N", "E", "S", "W"):
            waypoint = move(go, waypoint, amount, moves_dict)
        else:
            waypoint = turn(loc, go, waypoint, amount, moves_dict)
    return loc


if __name__ == "__main__":
    input_path = Path.cwd() / "day_12" / "input_day_12.txt"
    moves = open(input_path).read().split("\n")
    print("Part I")
    final_loc = read_moves_p1(moves)
    print(sum(final_loc))
    print("Part II")
    final_loc = read_moves_p2(moves)
    print(sum(final_loc))
