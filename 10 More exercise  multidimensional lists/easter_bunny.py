def bunny_movement(matrix_data):
    bunny_direction = None
    bunny_path = []
    total_eggs_collected = 0

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'B':

                for direction, position in directions.items():
                    bunny_row_pos = row + position[0]
                    bunny_col_pos = col + position[1]

                    current_eggs_collected = 0
                    current_bunny_path = []

                    while 0 <= bunny_row_pos < len(matrix_data) and 0 <= bunny_col_pos < len(matrix_data):

                        if matrix_data[bunny_row_pos][bunny_col_pos] == 'X':
                            break
                        current_eggs_collected += int(matrix_data[bunny_row_pos][bunny_col_pos])
                        current_bunny_path.append([bunny_row_pos, bunny_col_pos])

                        bunny_row_pos += position[0]
                        bunny_col_pos += position[1]

                    if current_eggs_collected >= total_eggs_collected:
                        total_eggs_collected = current_eggs_collected
                        bunny_path = current_bunny_path
                        bunny_direction = direction

    print(bunny_direction)
    print(*bunny_path, sep='\n')
    print(total_eggs_collected)


def matrix_func():
    size = int(input())
    curr_matrix = []
    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
bunny_movement(matrix)