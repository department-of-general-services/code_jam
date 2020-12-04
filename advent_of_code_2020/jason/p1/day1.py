import re

file = open('input.txt', 'r')
inputs = []
result = 0

for line in file:
    clean_line = re.sub(r"[\n\t\s]*", "", line)
    inputs.append(int(clean_line))

file.close()

for i in inputs:
    for j in inputs:
        if (i + j) == 2020:
            result = i * j

print(result)
