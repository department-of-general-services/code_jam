from pathlib import Path
import re


def parse(step):
    regex = r"^([a-z]{3})\s(\W[\d]*)"
    try:
        matches = re.match(regex, step).groups()
    except AttributeError:
        raise Exception(f"Problem with input {step}")
    return matches[0], int(matches[1])


def navigate(idx, ledger, acc, steps):
    # print(acc)
    instruction, arg = parse(steps[idx])
    # print(instruction)
    # print(idx)
    if idx in ledger:
        # print(f"Loop found.")
        return (acc, True)
    elif idx == len(steps) - 1:
        # print("Loop fixed.")
        return (acc, False)
    elif instruction == "acc":
        acc += arg
        ledger.add(idx)
        return navigate(idx + 1, ledger, acc, steps)
    elif instruction == "jmp":
        ledger.add(idx)
        return navigate(idx + arg, ledger, acc, steps)
    elif instruction == "nop":
        return navigate(idx + 1, ledger, acc, steps)


def find_loop(steps):
    acc = 0
    ledger = set()
    return navigate(0, ledger, acc, steps)


def try_switch(idx, steps):
    steps_new = steps.copy()
    if "jmp" in steps_new[idx]:
        steps_new[idx] = steps_new[idx].replace("jmp", "nop")
    if "nop" in steps[idx]:
        steps_new[idx] = steps_new[idx].replace("nop", "jmp")
    # print(f"Has steps changed? {steps != steps_new}")
    return find_loop(steps_new)


def test_swaps(steps):
    for idx in range(len(steps)):
        instruction, arg = parse(steps[idx])
        # print(f"Trying position {idx} for instruction {instruction}")
        if instruction in ["jmp", "nop"]:
            res = try_switch(idx, steps)
            if res[1] == False:
                print(res[0])


if __name__ == "__main__":
    input_path = Path.cwd() / "day_8" / "input_day_8.txt"
    steps = open(input_path).read().split("\n")

    print("Part I")
    test = find_loop(steps)
    print(test[0])

    print("Part II")
    test_swaps(steps)
