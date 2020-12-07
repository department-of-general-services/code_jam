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
        for second_entry in rest_of_entries:
            rest_of_entries = [item for item in entries if item != second_entry]
            for third_entry in rest_of_entries:
                if entry + second_entry + third_entry == 2020:
                    # print(f"Found it! {entry}, {second_entry}, {third_entry}")
                    return entry * second_entry * third_entry


@timer
def adds_to_2020_combinations(input_path):
    entries = open(input_path).read().splitlines()
    entries = list(map(int, entries))

    for trio in combinations(entries, r=3):
        if sum(trio) == 2020:
            # print(f"Found it! {trio[0]}, {trio[1]}, {trio[2]}")
            return trio[0] * trio[1] * trio[2]


if __name__ == "__main__":
    input_path = Path.cwd() / "day_1" / "input_day_1.txt"
    print("Running brute force method.")
    answer = adds_to_2020_brute_force(input_path)
    print(f"The answer is: {answer}")
    print("Running itertools method.")
    answer = adds_to_2020_combinations(input_path)
    print(f"The answer is: {answer}")