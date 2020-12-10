from pathlib import Path
import re
import numpy as np


def extract_container(string):
    regex = r"^.*?(?=(\ bag))"
    return re.search(regex, string)[0]


def extract_contained(string):
    regex = r"(?<=\d\s)(.*?)(?=\sbag)"
    return re.findall(regex, string)


def find_containers(obj, rules, ledger):
    for rule in rules:
        contained_colors = extract_contained(rule)
        if obj in contained_colors:
            container = extract_container(rule)
            ledger.add(container)
            find_containers(container, rules, ledger)
    return


def find_rule(obj, rules):
    rule = [rule for rule in rules if rule.startswith(obj)]
    return rule[0]


def extract_contained_and_counts(string):
    regex = r"(\d\s)(.*?)(?=\sbag)"
    return [(int(tup[0]), tup[1]) for tup in re.findall(regex, string)]


def count_leaves(path):
    counts = [tup[0] for tup in path]
    return np.product(counts)


def depth_search(path, list_of_paths, rules):
    leaf = path[-1]
    count, obj = leaf[0], leaf[1]
    rule = find_rule(obj, rules)
    contained = extract_contained_and_counts(rule)

    if len(contained) < 1:
        list_of_paths.append(path)
    else:
        for tup in contained:
            new_path = path + [tup]
            depth_search(new_path, list_of_paths, rules)


def remove_duplicates(list_of_paths):
    return [list(tup) for tup in {tuple(path) for path in list_of_paths}]


if __name__ == "__main__":
    input_path = Path.cwd() / "day_7" / "input_day_7.txt"
    rules = open(input_path).read().split("\n")

    print("Part I")
    ledger = set()
    objective = "shiny gold"
    find_containers(objective, rules, ledger)
    print(len(ledger))

    print("Part II")
    path = [(1, "shiny gold")]
    list_of_paths = []
    depth_search(path, list_of_paths, rules)

    leaf_counts = []
    max_depth = max([len(path) for path in list_of_paths])
    for idx in range(max_depth, 1, -1):
        list_of_paths = remove_duplicates(list_of_paths)
        for path in list_of_paths:
            if len(path) >= idx:
                prod = count_leaves(path)
                leaf_counts.append(prod)
                leaf = path.pop()
                print(f"Counted {prod} bags of color: {leaf[1]}.")

    print(f"Total bags required inside of shiny gold bag: {sum(leaf_counts)}")
