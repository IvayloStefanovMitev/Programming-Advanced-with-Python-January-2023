def movement_func(matrix_data):

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }
    my_pos = []
    touched_opponents = 0
    moves_made = 0
    players = 3
    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'B':
                my_pos = [row, col]
                matrix_data[row][col] = '-'

    while players:
        direction = input()

        if direction == "Finish":
            break

        my_pos_row = my_pos[0] + directions[direction][0]
        my_pos_col = my_pos[1] + directions[direction][1]

        if not (0 <= my_pos_row < len(matrix_data) and 0 <= my_pos_col < len(matrix_data)):
            continue
        elif matrix_data[my_pos_row][my_pos_col] == 'O':
            continue

        moves_made += 1

        if matrix_data[my_pos_row][my_pos_col] == 'P':
            touched_opponents += 1
            players -= 1
            my_pos = [my_pos_row, my_pos_col]
            matrix_data[my_pos_row][my_pos_col] = "-"
        else:
            my_pos = [my_pos_row, my_pos_col]

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


def matrix_func():
    rows, cols = map(int, input().split())
    curr_matrix = []
    for row in range(rows):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
movement_func(matrix)