import functions_path as fnc

# Advent of code
# --- Day 6: Guard Gallivant ---

if __name__ == '__main__':
    # look into the file
    lab_symbols = fnc.read_input("input.txt")
    _, lab = fnc.create_bool_matrix(lab_symbols, '#')
    idxs, _ = fnc.create_bool_matrix(lab_symbols, '^')
    start_row, start_col = idxs[0]
    l_rows = len(lab)
    l_cols = len(lab[0])
    len_matrix = l_rows * l_cols
    # Guard is in cycle
    guard_is_cycled = 0
    # Define cycles for brute force
    for i in range(0, l_rows):
        for j in range(0, l_cols):

            # Skip first position
            if (i, j) == (start_row, start_col):
                continue
            # Initialize lab
            lab_symbols = fnc.read_input("input.txt")
            n, lab = fnc.create_bool_matrix(lab_symbols, '#')
            # Place one more obstacle
            lab[i][j] = False
            # path of guard
            idxs, path = fnc.create_bool_matrix(lab_symbols, '^')
            # Initialize directions
            up = True  # start going up
            down = False
            right = False
            left = False
            # First position
            column = idxs[0][1]
            row = idxs[0][0]
            # Look how many times the cycle
            steps = 0
            # while guard going
            visited_positions = set()
            while True:
                # Check if row and column are within bounds
                if row < 0 or row >= len(lab) or column < 0 or column >= len(lab[0]):
                    break  # Exit the loop
                steps += 1
                # if steps > 15*len_matrix:
                #     guard_is_cycled += 1
                #     break
                if (row, column) in visited_positions:  # Check if current position is visited
                    guard_is_cycled += 1
                    break
                visited_positions.add((row, column))  # Add current position to visited set
                lab, path, row, column, up, right, down, left =  \
                    fnc.check_all_directions(lab, path, row, column, up, right, down, left)
                if len(visited_positions) >= len(lab) * len(lab[0]):
                    break  # Guard hasn't found a loop after visiting all positions
            # if steps > 15*len_matrix:
            #     break

    print('Final number of barrier for guard to go in circles is', guard_is_cycled, '.')
