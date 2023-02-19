def alice_movement(matrix_data):
    tea_bags = 0
    alice_pos = []
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'A':
                alice_pos = [row, col]
                matrix_data[row][col] = '*'
                break
        break

    while tea_bags < 10:
        direction = input()

        alice_row_pos = alice_pos[0] + directions[direction][0]
        alice_col_pos = alice_pos[1] + directions[direction][1]

        if not (0 <= alice_row_pos < len(matrix_data) and 0 <= alice_col_pos < len(matrix_data)):
            break

        alice_pos = [alice_row_pos, alice_col_pos]
        new_alice_position = matrix_data[alice_row_pos][alice_col_pos]
        matrix_data[alice_row_pos][alice_col_pos] = '*'

        if new_alice_position == 'R':

            break

        if new_alice_position.isdigit():
            tea_bags += int(new_alice_position)

    if tea_bags >= 10:
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")
    print(*[' '.join(row) for row in matrix_data], sep='\n')


def matrix_func():
    size = int(input())
    curr_matrix = []
    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
alice_movement(matrix)



# def alice_movement(matrix_data):
#     tea_bags = 0
#     alice_pos = []
#     directions = {
#         'up': (-1, 0),
#         'down': (1, -0),
#         'left': (0, -1),
#         'right': (0, 1),
#     }
#
#     for row in range(len(matrix_data)):
#         for col in range(len(matrix_data)):
#             if matrix_data[row][col] == 'A':
#                 alice_pos = [row, col]
#                 matrix_data[row][col] = '*'
#
#                 while tea_bags < 10:
#                     direction = input()
#
#                     alice_row_pos = row + directions[direction][0]
#                     alice_col_pos = col + directions[direction][1]
#
#                     if not (0 <= alice_row_pos < len(matrix_data) and 0 <= alice_col_pos < len(matrix_data)):
#
#                         break
#
#                     alice_pos = [alice_row_pos, alice_col_pos]
#                     new_alice_position = matrix_data[alice_row_pos][alice_col_pos]
#                     matrix_data[alice_row_pos][alice_col_pos] = '*'
#
#                     if new_alice_position == 'R':
#                         print("Alice didn't make it to the tea party.")
#                         break
#
#                     if new_alice_position.isdigit():
#                         tea_bags += int(new_alice_position)
#
#                 if tea_bags >= 10:
#                     print("She did it! She went to the party.")
#                 else:
#                     print("Alice didn't make it to the tea party.")
#                 print(*[' '.join(row) for row in matrix_data], sep='\n')
#
#
# def matrix_func():
#     size = int(input())
#     curr_matrix = []
#     for row in range(size):
#         row_data = input().split()
#         curr_matrix.append(row_data)
#
#     return curr_matrix
#
#
# matrix = matrix_func()
# alice_movement(matrix)