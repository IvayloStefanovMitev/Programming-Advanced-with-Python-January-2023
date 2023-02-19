def battlefield(matrix_data):
    hit_counter = 0
    battle_cruiser = 3
    submarine_pos = []

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == "S":
                submarine_pos = [row, col]
                matrix_data[row][col] = "-"

    while battle_cruiser:
        direction = input()

        submarine_pos_row = submarine_pos[0] + directions[direction][0]
        submarine_pos_col = submarine_pos[1] + directions[direction][1]

        submarine_pos = [submarine_pos_row, submarine_pos_col]

        if matrix_data[submarine_pos_row][submarine_pos_col] == "*":
            hit_counter += 1
            if hit_counter == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos_row}, {submarine_pos_col}]!")
                break
            matrix_data[submarine_pos_row][submarine_pos_col] = "-"

        elif matrix_data[submarine_pos_row][submarine_pos_col] == "C":
            battle_cruiser -= 1
            matrix_data[submarine_pos_row][submarine_pos_col] = "-"
    else:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

    matrix_data[submarine_pos[0]][submarine_pos[1]] = "S"
    print(*["".join(row) for row in matrix_data], sep="\n")


def matrix_func():
    size = int(input())

    curr_matrix = []

    for row in range(size):
        row_data = list(input())
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
battlefield(matrix)
