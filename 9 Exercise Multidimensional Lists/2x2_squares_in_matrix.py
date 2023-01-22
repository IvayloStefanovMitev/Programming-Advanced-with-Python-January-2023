def squares_matrix_func(matrix_data):
    equal_blocks = 0
    matrix_row = len(matrix_data)
    matrix_rol = len(matrix_data[0])
    for row in range(matrix_row - 1):
        for col in range(matrix_rol - 1):
            symbol = matrix_data[row][col]

            if matrix_data[row][col + 1] == symbol and matrix_data[row + 1][col] == symbol and\
                    matrix_data[row + 1][col + 1] == symbol:
                equal_blocks += 1

    print(equal_blocks)


def matrix_func():
    rows, cols = map(int, input().split())
    curr_matrix = []
    for row in range(rows):
        row_data = list(input().split())
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
squares_matrix_func(matrix)