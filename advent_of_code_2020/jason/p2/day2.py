import re

file = open('input.txt', 'r')
inputs = []
valid_count = 0

def is_valid_pw(search, min_val, max_val, input_str):
    count = input_str.count(search)
    if count in range(min_val, max_val + 1):
        return True
    else:
        return False

for line in file:
    clean_line = re.sub(r"[\n]*", "", line)
    inputs.append(clean_line)

for input in inputs:
    exploded = input.split()
    letter = re.sub(r":", "", exploded[1])
    minVal = int(exploded[0].split("-")[0])
    maxVal = int(exploded[0].split("-")[1])
    arg = exploded[2]
    if is_valid_pw(letter, minVal, maxVal, arg):
        valid_count = valid_count + 1

print('there are ' + str(valid_count) + ' valid passwords')