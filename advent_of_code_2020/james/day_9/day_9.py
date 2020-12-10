import numpy as np
from pathlib import Path
from itertools import combinations


def extract_windows(array, window_size):
    # vectorized approach to get all windows in one act of indexing
    max_idx = len(array) - window_size

    sub_windows = (
        np.expand_dims(np.arange(window_size), 0)
        + np.expand_dims(np.arange(max_idx + 1), 0).T
    )

    return array[sub_windows]


def find_products(array, window_size):
    acc = []
    for idx, arr in enumerate(array):
        combos = combinations(arr, r=2)
        prods = [sum(tup) for tup in combos]
        acc.append((prods, idx + window_size))
    return acc


def detect_weakness(list_, sums):
    for tup in list_:
        if sums[tup[1]] not in tup[0]:
            return sums[tup[1]]


def all_contiguous_regions(array):
    return [
        array[i : i + j]
        for i in range(0, len(array))
        for j in range(1, len(array) - i + 1)
    ]


def check_regions(regions, num):
    for region in regions:
        if region.sum() == num:
            return np.min(region) + np.max(region)


if __name__ == "__main__":
    input_path = Path.cwd() / "day_9" / "input_day_9.txt"
    nums = open(input_path).read().split("\n")
    nums = np.array([int(num) for num in nums])

    print("Part I")
    window_size = 25
    slices = extract_windows(nums, window_size)
    sums = find_products(slices, window_size)
    invalid_number = detect_weakness(sums, nums)
    print(invalid_number)

    print("Part II")
    regions = all_contiguous_regions(nums)
    sum_min_max = check_regions(regions, invalid_number)
    print(sum_min_max)
