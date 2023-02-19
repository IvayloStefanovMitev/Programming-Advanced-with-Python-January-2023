def subtract_func(row, col, value, matrix_data):
    if 0 <= row < len(matrix_data) and 0 <= col < len(matrix_data):
        matrix_data[row][col] -= value
    else:
        print("Invalid coordinates")

    return matrix_data


def add_func(row, col, value, matrix_data):
    if 0 <= row < len(matrix_data) and 0 <= col < len(matrix_data):
        matrix_data[row][col] += value
    else:
        print("Invalid coordinates")

    return matrix_data


def command_func(matrix_data):

    while True:
        command = input().split()

        if command[0] == 'END':
            break

        elif command[0] == 'Add':
            row, col, value = command[1], command[2], command[3]
            matrix_data = add_func(int(row), int(col), int(value), matrix_data)

        elif command[0] == 'Subtract':
            row, col, value = command[1], command[2], command[3]
            matrix_data = subtract_func(int(row), int(col), int(value), matrix_data)

    return matrix_data


def matrix_func():
    size = int(input())

    curr_matrix = []
    for row in range(size):
        row_data = list(map(int, input().split()))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
commands = command_func(matrix)
for curr_row in matrix:
    print(*curr_row)

# [print(*curr_row) for curr_row in matrix]
