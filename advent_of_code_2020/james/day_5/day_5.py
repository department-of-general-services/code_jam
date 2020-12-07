from pathlib import Path


def split_vector(vector, location):
    half = len(vector) // 2
    if location in ["F", "L"]:
        return vector[:half]  # lower-numbered half
    elif location in ["B", "R"]:
        return vector[half:]  # higher-numbered half


def binary_search(max_val, b_pass):
    vector = [val for val in range(0, max_val)]
    for char in b_pass:
        vector = split_vector(vector, char)
    return vector[0]


def b_pass_to_row_id(b_pass):
    row = binary_search(128, b_pass[:7])
    col = binary_search(8, b_pass[7:])
    return row * 8 + col


if __name__ == "__main__":
    input_path = Path.cwd() / "day_5" / "input_day_5.txt"
    data_raw = open(input_path).read().split("\n")

    row_ids = [b_pass_to_row_id(b_pass) for b_pass in data_raw]
    print("Part I")
    print(max(row_ids))
    print("Part II")
    # use set difference to find missing id
    print(set(range(min(row_ids), max(row_ids))) - set(row_ids))