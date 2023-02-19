def read_func(direction, first_position, directions, matrix_data):

    curr_row = first_position[0] + directions[direction][0]
    curr_col = first_position[1] + directions[direction][1]

    curr_pos = [curr_row, curr_col]
    first_position = curr_pos

    if matrix_data[curr_row][curr_col].isalnum():
        print(matrix_data[curr_row][curr_col])

    return matrix_data, first_position


def delete_func(direction, first_position, directions, matrix_data):
    curr_row = first_position[0] + directions[direction][0]
    curr_col = first_position[1] + directions[direction][1]

    curr_pos = [curr_row, curr_col]
    first_position = curr_pos

    if matrix_data[curr_row][curr_col].isalnum():
        matrix_data[curr_row][curr_col] = '.'

    return matrix_data, first_position


def update_func(direction, value, first_position, directions, matrix_data):

    curr_row = first_position[0] + directions[direction][0]
    curr_col = first_position[1] + directions[direction][1]

    curr_pos = [curr_row, curr_col]
    first_position = curr_pos

    if matrix_data[curr_row][curr_col].isalnum():
        matrix_data[curr_row][curr_col] = value

    return matrix_data, first_position


def create_func(direction, value, first_position, directions, matrix_data):

    curr_row = first_position[0] + directions[direction][0]
    curr_col = first_position[1] + directions[direction][1]

    curr_pos = [curr_row, curr_col]
    first_position = curr_pos

    if matrix_data[curr_row][curr_col] == '.':
        matrix_data[curr_row][curr_col] = value

    return matrix_data, first_position


def main_logic_func(matrix_data):
    first_position = list(int(el) for el in input() if el.isdigit())

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    while True:
        command = input().split(', ')

        if command[0] == 'Stop':
            break

        elif command[0] == 'Create':
            direction, value = command[1], command[2]
            matrix_data, first_position = create_func(direction, value, first_position, directions, matrix_data)

        elif command[0] == 'Update':
            direction, value = command[1], command[2]
            matrix_data, first_position = update_func(direction, value, first_position, directions, matrix_data)

        elif command[0] == 'Delete':
            direction = command[1]
            matrix_data, first_position = delete_func(direction, first_position, directions, matrix_data)

        elif command[0] == 'Read':
            direction = command[1]
            matrix_data, first_position = read_func(direction, first_position, directions, matrix_data)

    print(*[' '.join(row) for row in matrix_data], sep='\n')


def matrix_func():
    size = 6
    curr_matrix = []
    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
main_logic_func(matrix)