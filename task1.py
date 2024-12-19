import functions_path as fnc

# Advent of code
# --- Day 6: Guard Gallivant ---

if __name__ == '__main__':
    # Read and close file
    lab_symbols = fnc.read_input("input.txt")
    n, lab = fnc.create_bool_matrix(lab_symbols, '#')
    idxs, path = fnc.create_bool_matrix(lab_symbols, '^')
    # Initialize directions
    up = True  # start going up
    down = False
    right = False
    left = False
    # First position
    column = idxs[0][1]
    row = idxs[0][0]

    while True:
        # Check if row and column are within bounds
        if row < 0 or row >= len(lab) or column < 0 or column >= len(lab[0]):
            break  # Exit the loop

        lab, path, row, column, up, right, down, left =  \
            fnc.check_all_directions(lab, path, row, column, up, right, down, left)

    print('Final number of steps is', fnc.count_false(path), '.')



