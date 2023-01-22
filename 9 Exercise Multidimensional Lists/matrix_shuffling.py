def check_valid_func(valid_rows, valid_cols, data):
    if set(data[:2]).issubset(valid_rows) and set(data[2:]).issubset(valid_cols):
        return True
    return False


def swap_func(command, data, valid_rows, valid_cols):

    if check_valid_func(valid_rows, valid_cols, data) and command == "swap" and len(data) == 4:
        row1, col1, row2, col2 = data
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(matrix[row][col], end=' ')
            print()
    else:
        print('Invalid input!')


def command_func(matrix_data):
    valid_rows = range(len(matrix_data))
    valid_cols = range(len(matrix_data[0]))

    while True:
        command, *data = [int(n) if n.isdigit() else n for n in input().split()]

        if command == "END":
            break

        swap_func(command, data, valid_rows, valid_cols)
        check_valid_func(valid_rows, valid_cols, data)


def func_matrix():
    rows, cols = map(int, input().split())
    curr_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split()))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = func_matrix()
command_func(matrix)
