from pathlib import Path
import re


def str_to_dict(str):
    key_vals = str.replace("\n", " ").split(" ")
    return dict(map(lambda s: s.split(":"), key_vals))


def test_keys(passport):
    full_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    acceptable_keys = [key for key in full_keys if key != "cid"]
    if all(key in passport for key in full_keys) or all(
        key in passport for key in acceptable_keys
    ):
        return True
    else:
        return False


def check_byr(byr):
    return len(byr) == 4 and (1920 <= int(byr) <= 2002)


def check_iyr(iyr):
    return len(iyr) == 4 and (2010 <= int(iyr) <= 2020)


def check_eyr(eyr):
    return len(eyr) == 4 and (2020 <= int(eyr) <= 2030)


def check_hgt(hgt):
    regex = r"^(\d+)(in|cm)"
    match = re.match(regex, hgt)
    if match:
        if match.groups()[1] == "cm":
            if 150 <= int(match.groups()[0]) <= 193:
                return True
        if match.groups()[1] == "in":
            if 59 <= int(match.groups()[0]) <= 76:
                return True


def check_hcl(hcl):
    regex = r"^#[0-9|a-f]{6}$"
    if re.match(regex, hcl):
        return True


def check_ecl(ecl):
    colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    return ecl in colors


def check_pid(pid):
    regex = r"^[0-9]{9}$"
    if re.match(regex, pid):
        return True


def test_values(passport):
    if (
        check_byr(passport.get("byr"))
        and check_iyr(passport.get("iyr"))
        and check_eyr(passport.get("eyr"))
        and check_hgt(passport.get("hgt"))
        and check_hcl(passport.get("hcl"))
        and check_ecl(passport.get("ecl"))
        and check_pid(passport.get("pid"))
    ):
        return True


if __name__ == "__main__":
    input_path = Path.cwd() / "day_4" / "input_day_4.txt"
    data_raw = open(input_path).read().split("\n\n")

    valid_count = 0
    for passport in data_raw:
        passport_dict = str_to_dict(passport)
        if test_keys(passport_dict) and test_values(passport_dict):
            valid_count += 1
    print(valid_count)