
# Advent of code
# --- Day 6: Guard Gallivant ---

def read_input(filename: str):

    with open(filename, 'r') as f:
        rows = f.readlines()

    return rows


# def create_bool_matrix(rows, pattern:str):

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

def count_true(matrix):
    count = 0
    for row in matrix:
        count += row.count(True)  # Count True values in each row
    return count

if __name__ == '__main__':
    # Read and close file
    lab_symbols = read_input("input.txt")
    n, lab = create_bool_matrix(lab_symbols, '#')
    idxs, path = create_bool_matrix(lab_symbols, '^')
    print(idxs)
    # Initialize directions
    up = True
    down = False
    right = False
    left = False
    # First position
    column = idxs[0][1]
    row = idxs[0][0]
    krok = 0
    while True:
        # Check if row and column are within bounds
        if row < 0 or row >= len(lab) or column < 0 or column >= len(lab[0]):
            break  # Exit the loop
        if up:
            if lab[row][column]:
                path[row][column] = True
                row = row - 1
            else:
                up = False
                right = True
                column = column + 1
                row = row + 1
        elif right:
            if lab[row][column]:
                path[row][column] = True
                column = column + 1
            else:
                right = False
                down = True
                column = column - 1
                row = row + 1
        elif down:
            if lab[row][column]:
                path[row][column] = True
                row = row + 1
            else:
                down = False
                left = True
                column = column - 1
                row = row - 1
        elif left:
            if lab[row][column]:
                path[row][column] = True
                column = column - 1
            else:
                down = False
                left = True
                column = column + 1
                row = row - 1

    print('Final number of steps is', count_true(path), '.')

