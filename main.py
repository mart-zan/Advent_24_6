
# Advent of code
# --- Day 6: Guard Gallivant ---

def read_input(filename: str):

    with open(filename, 'r') as f:
        rows = f.readlines()

    return rows


def create_bool_matrix(rows, pattern:str):

    bool_matrix = []
    for i, line in enumerate(rows):
        print(line)

        bool_row = []
        for j, symbol in enumerate(line.strip()):
            print(symbol)
            if symbol == pattern:
                # print('je tu hash')
                bool_row.append(True)
            else:
                # print('je tu tecka')
                bool_row.append(False)
            # print('------')
        bool_matrix.append(bool_row)

    return bool_matrix


if __name__ == '__main__':
    # Read and close file
    lab = read_input("input.txt")
    bool_hash = create_bool_matrix(lab, '#')
    # print(lab)
    # print(bool_hash)
