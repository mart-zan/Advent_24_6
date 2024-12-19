import functions_path as fnc

# Advent of code
# --- Day 6: Guard Gallivant ---

if __name__ == '__main__':
    # Read input once
    lab_symbols = fnc.read_input("input.txt")
    _, original_lab = fnc.create_bool_matrix(lab_symbols, '#')
    idxs, _ = fnc.create_bool_matrix(lab_symbols, '^')
    start_row, start_col = idxs[0]

    l_rows = len(original_lab)
    l_cols = len(original_lab[0])
    len_matrix = l_rows * l_cols

    # Counter for positions where guard gets stuck in a loop
    guard_is_cycled = 0

    # Try placing an obstruction at every position
    for i in range(l_rows):
        for j in range(l_cols):
            steps = 0
            # Skip starting position
            if (i, j) == (start_row, start_col):
                continue

            # Create a copy of the lab and place an obstruction
            lab = original_lab
            lab[i][j] = False  # Place obstruction

            # Initialize guard path and directions
            row, col = start_row, start_col
            path = [[False] * l_cols for _ in range(l_rows)]  # Track visited positions
            up, right, down, left = True, False, False, False

            visited_positions = set()

            while True:

                # Check if out of bounds
                if row < 0 or row >= l_rows or col < 0 or col >= l_cols:
                    break

                # Detect loop by revisiting positions
                if (row, col, up, right, down, left) in visited_positions:
                    guard_is_cycled += 1
                    break
                visited_positions.add((row, col, up, right, down, left))

                # Mark current position as visited
                path[row][col] = True

                # Move the guard based on the rules
                if up and row > 0 and lab[row - 1][col]:
                    row -= 1
                elif right and col < l_cols - 1 and lab[row][col + 1]:
                    col += 1
                elif down and row < l_rows - 1 and lab[row + 1][col]:
                    row += 1
                elif left and col > 0 and lab[row][col - 1]:
                    col -= 1
                else:
                    # Change direction if obstacle is in front
                    if up:
                        up, right = False, True
                    elif right:
                        right, down = False, True
                    elif down:
                        down, left = False, True
                    elif left:
                        left, up = False, True

            steps += 1
            if steps > 15 * len_matrix:  # Fail-safe for infinite loops
                break

    print('Final number of barriers for guard to go in circles is', guard_is_cycled, '.')
