import functools
import time
from pathlib import Path
from itertools import combinations


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        times = 10
        tic = time.perf_counter()
        for iteration in range(times):
            value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = (toc - tic) / times
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value

    return wrapper_timer


@timer
def adds_to_2020_brute_force(input_path):
    entries = open(input_path).read().splitlines()
    entries = list(map(int, entries))

    for entry in entries:
        rest_of_entries = [item for item in entries if item != entry]
        for other in rest_of_entries:
            if entry + other == 2020:
                # print(f"Found it! {entry}, {other}")
                return entry * other


@timer
def adds_to_2020_combinations(input_path):
    entries = open(input_path).read().splitlines()
    entries = list(map(int, entries))

    for pair in combinations(entries, r=2):
        if sum(pair) == 2020:
            # print(f"Found it! {pair[0]}, {pair[1]}")
            return pair[0] * pair[1]


if __name__ == "__main__":
    input_path = Path.cwd() / "day_one" / "input_day_1.txt"
    answer = adds_to_2020_brute_force(input_path)
    answer = adds_to_2020_combinations(input_path)

    print(f"The answer is: {answer}")