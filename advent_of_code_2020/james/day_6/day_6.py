from pathlib import Path


def count_uniques(input):
    unique_chars = set(input.replace("\n", ""))
    return len(unique_chars)


def count_unanimous(input):
    count = 0
    unique_chars = set(input.replace("\n", ""))
    responses = input.split("\n")
    for char in unique_chars:
        if all(char in response for response in responses):
            count += 1
    return count


if __name__ == "__main__":
    input_path = Path.cwd() / "day_6" / "input_day_6.txt"
    data_raw = open(input_path).read().split("\n\n")

    print("Part I")
    yes_counts = [count_uniques(responses) for responses in data_raw]
    print(sum(yes_counts))
    print("Part II")
    unanimous_counts = [count_unanimous(responses) for responses in data_raw]
    print(sum(unanimous_counts))