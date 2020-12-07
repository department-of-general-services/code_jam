import functools
import time
from pathlib import Path
from itertools import combinations
import pandas as pd
import re


def split_input(row):
    regex = r"^(\d+)-(\d+)\s(\w):\s(\w+)"
    match = re.match(pattern=regex, string=row["raw_text"])
    row["min_reps"] = int(match.groups()[0])
    row["max_reps"] = int(match.groups()[1])
    row["target_char"] = match.groups()[2]
    row["password"] = match.groups()[3]
    return row


def is_password_legit(row):
    # count the number of times the char in question appears
    row["count"] = row["password"].count(row["target_char"])
    # check that the count is not less than the min or more than the max
    row["is_valid"] = row["min_reps"] <= row["count"] <= row["max_reps"]
    return row


def is_password_legit_part_II(row):
    # rename the changed cols to avoid confusion
    row = row.rename({"min_reps": "pos_1", "max_reps": "pos_2"})
    # switch to 0-based indexing
    row["pos_1"] = row["pos_1"] - 1
    row["pos_2"] = row["pos_2"] - 1
    # creating boolean columns for positions 1 & 2
    row["is_in_pos_1"] = row["password"][row["pos_1"]] == row["target_char"]
    row["is_in_pos_2"] = row["password"][row["pos_2"]] == row["target_char"]
    # the two boolean cols need to sum to 1 (exclusive or)
    row["is_valid"] = sum(row[["is_in_pos_1", "is_in_pos_2"]]) == 1
    return row


if __name__ == "__main__":
    input_path = Path.cwd() / "day_2" / "input_day_2.txt"
    passwords = open(input_path).read().splitlines()
    df = pd.DataFrame(passwords, columns=["raw_text"])
    df_split = df.apply(split_input, axis=1)

    ### Part I
    res_df = df_split.apply(is_password_legit, axis=1)
    print("Part I")
    print(f"Of {len(res_df)} passwords, {res_df['is_valid'].sum()} are legit.")

    ### Part II
    res_df_2 = df_split.apply(is_password_legit_part_II, axis=1)
    print("Part II")
    print(f"Of {len(res_df_2)} passwords, {res_df_2['is_valid'].sum()} are legit.")