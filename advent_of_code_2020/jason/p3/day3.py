import re
import math


def build_matrix(input_file_path, steps):
    file = open(input_file_path, 'r')
    matrix = []
    cols_in_input = 0
    rows_in_input = 0
    for line in file:
        cols_in_input = len(line)
        rows_in_input += 1

    input_clones_needed = math.ceil(rows_in_input/(cols_in_input / steps))

    file.seek(0)

    for line in file:
        clean_line = re.sub(r"[\n\t\s]*", "", line)
        cloned_line = ''
        row = []

        for i in range(0, input_clones_needed):
            cloned_line = cloned_line + clean_line

        for i in range(0, len(cloned_line)):
            row.append(cloned_line[i])

        matrix.append(row)

    file.close()
    return matrix


if __name__ == "__main__":

    steps_right = 3
    matrix = build_matrix('input.txt', steps_right)
    number_of_trees = 0
    current_row = 0
    current_col = 0

    for row in matrix:
        if matrix[current_row][current_col] == '#':
            number_of_trees = number_of_trees + 1
        current_row += 1
        current_col += steps_right

    print('we hit ' + str(number_of_trees) + ' trees')
