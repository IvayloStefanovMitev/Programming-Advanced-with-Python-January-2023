def movement_func(matrix_data, names_player):
    first_player = names_player[0]
    second_player = names_player[1]
    counter_tom = 0
    counter_jerry = 0
    player_hit_tom = None
    player_hit_jerry = None

    while True:

        position = list(int(num) for num in input() if num.isdigit())
        if (counter_tom == 1 and player_hit_tom == first_player) or \
                (counter_jerry == 1 and player_hit_jerry == first_player):
            if first_player == 'Tom':
                counter_tom = 0
                player_hit_tom = None
            else:
                counter_jerry = 0
                player_hit_jerry = None
            first_player, second_player = second_player, first_player
            continue

        elif 0 <= position[0] < len(matrix_data) and 0 <= position[1] < len(matrix_data):
            if matrix_data[position[0]][position[1]] == 'E':
                print(f"{first_player} found the Exit and wins the game!")
                break
            elif matrix_data[position[0]][position[1]] == 'W':
                if first_player == 'Tom':
                    counter_tom = 1
                    player_hit_tom = first_player
                else:
                    counter_jerry = 1
                    player_hit_jerry = first_player
                print(f"{first_player} hits a wall and needs to rest.")
            elif matrix_data[position[0]][position[1]] == 'T':
                print(f"{first_player} is out of the game! The winner is {second_player}.")
                break
        first_player, second_player = second_player, first_player


def matrix_func():
    size = 6
    curr_matrix = []

    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


names = input().split(', ')
matrix = matrix_func()
movement_func(matrix, names)