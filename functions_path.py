def create_bool_matrix(rows, pattern: str):
    bool_matrix = []
    symbol_indexes = []

    for i, line in enumerate(rows):
        bool_row = []
        for j, symbol in enumerate(line.strip()):
            if symbol == pattern:
                bool_row.append(False)
                symbol_indexes.append([i, j])  # Store the index of the symbol
            else:
                bool_row.append(True)
        bool_matrix.append(bool_row)

    return symbol_indexes, bool_matrix

def count_false(matrix):
    count = 0
    for row in matrix:
        count += row.count(False)  # Count True values in each row
    return count

def check_all_directions(lab, path, row, column, up, right, down, left):

    if up:
        if lab[row][column]:
            path[row][column] = False
            row = row - 1
        else:
            up = False
            right = True
            column = column + 1
            row = row + 1
    elif right:
        if lab[row][column]:
            path[row][column] = False
            column = column + 1
        else:
            right = False
            down = True
            column = column - 1
            row = row + 1
    elif down:
        if lab[row][column]:
            path[row][column] = False
            row = row + 1
        else:
            down = False
            left = True
            column = column - 1
            row = row - 1
    elif left:
        if lab[row][column]:
            path[row][column] = False
            column = column - 1
        else:
            left = False
            up = True
            column = column + 1
            row = row - 1
    return lab, path, row, column, up, right, down, left
