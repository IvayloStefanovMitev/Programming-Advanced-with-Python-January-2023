def shoot_func(direction, directions, shooter_pos, matrix_data):
    shooting_pos_row = shooter_pos[0] + directions[direction][0]
    shooting_pos_col = shooter_pos[1] + directions[direction][1]

    while 0 <= shooting_pos_row < len(matrix_data) and 0 <= shooting_pos_col < len(matrix_data):

        if matrix_data[shooting_pos_row][shooting_pos_col] == 'x':
            matrix_data[shooting_pos_row][shooting_pos_col] = '.'

            return [shooting_pos_row, shooting_pos_col]

        shooting_pos_row += directions[direction][0]
        shooting_pos_col += directions[direction][1]


def move_func(direction, directions, steps, shooter_pos, matrix_data):
    shooter_pos_row = shooter_pos[0] + (directions[direction][0] * int(steps))
    shooter_pos_col = shooter_pos[1] + (directions[direction][1] * int(steps))

    if not (0 <= shooter_pos_row < len(matrix_data) and 0 <= shooter_pos_col < len(matrix_data)):
        return shooter_pos
    if matrix_data[shooter_pos_row][shooter_pos_col] == 'x':
        return shooter_pos

    return [shooter_pos_row, shooter_pos_col]


def shooting_func(matrix_data):

    shooter_pos = []
    targets = 0
    shooted_target_pos = []
    targets_hit = 0

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'A':
                shooter_pos = [row, col]
    for row in range(len(matrix_data)):
        if 'x' in matrix_data[row]:
            targets += matrix_data[row].count('x')

    number_of_commands = int(input())

    for number in range(number_of_commands):
        command = input().split()

        if command[0] == 'move':
            direction, steps = command[1], command[2]
            shooter_pos = move_func(direction, directions, steps, shooter_pos, matrix_data)

        elif command[0] == 'shoot':
            direction = command[1]
            shooted_target = shoot_func(direction, directions, shooter_pos, matrix_data)

            if shooted_target:
                targets_hit += 1
                shooted_target_pos.append(shooted_target)

            if targets == targets_hit:
                print(f"Training completed! All {targets} targets hit.")
                break

    if targets_hit < targets:
        print(f"Training not completed! {targets - targets_hit} targets left.")
    [print(row) for row in shooted_target_pos]


def matrix_func():
    size = 5
    curr_matrix = []
    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
shooting_func(matrix)

# def move(direction, steps):  # създаваме фунцкия move, първи параметър посоката и втори стъпките int
#     r = my_position[0] + (directions[direction][0] * steps)  # намираме реда и колоната като умножаваме стойностите от
#     c = my_position[1] + (directions[direction][1] * steps)  # посоката по стъпките и събираме с текущите координати
#
#     if not (0 <= r < size and 0 <= c < size):  # проверяваме дали позицията, на която искаме да стъпим е валидна
#         return my_position  # ако не е, връщаме текущата позиция
#     if field[r][c] == 'x':  # проверяваме дали на позицията, на която искаме да стъпим има мишена
#         return my_position  # ако да, връщаме текущата позиция
#
#     return [r, c]  # връщаме новата позиция
#
#
# def shoot(direction):  # създаваме фунцкия shoot, параметър посоката на стрелба
#     r = my_position[0] + directions[direction][0]  # намираме реда и колоната като събираме координатите от посоката
#     c = my_position[1] + directions[direction][1]  # с тези, на които се намираме
#
#     while 0 <= r < size and 0 <= c < size:  # развъртаме цикъл докато координатите са валидни
#         if field[r][c] == 'x':  # проверяваме дали куршума е достигнал мишена
#             field[r][c] = '.'  # ако да, заменяме х с точка
#             return [r, c]  # връщаме позицията на улучената мишена
#
#         r += directions[direction][0]  # събираме координатите от посоката
#         c += directions[direction][1]  # с тези, на които се намира куршума
#
#
# size = 5  # запазваме размера на матрицата в променлива
# field = []  # създаваме променлива, в която да пазим матрицата
#
# targets = 0  # създаваме променлива, в която да пазим броя на мишените в полето
# targets_hit = 0  # създаваме променлива, в която да пазим броя на уцелените мишени
# targets_hit_positions = []  # създаваме променлива, в която да пазим координатите на уцелените мишени
#
# my_position = []  # създаваме променлива, в която да пазим позицията ни
#
# directions = {  # създаваме променлива, в която да пазим посоките
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
#     field.append(input().split())  # прочитаме ред от конзолата, разделяме го по спейс и го добавяме към матрицата
#
#     if 'A' in field[row]:  # проверяваме дали нашата позиция се намира на този ред
#         my_position = [row, field[row].index('A')]  # запазваме нашата позиция
#         field[row][my_position[1]] = '.'  # променяме стойността на позицията ни в матрицата на точка
#     if 'x' in field[row]:  # проверяваме дали на реда има мишени
#         targets += field[row].count('x')  # увеличаваме броя на мишените с броя им на реда
#
# for _ in range(int(input())):  # развъртаме цикъл за очаквания брой команди
#     command_info = input().split()  # прочитаме командата и я разделяме по спейс
#
#     if command_info[0] == 'move':  # проверяваме дали командата е move
#         my_position = move(command_info[1], int(command_info[2]))  # извикваме функцията move, стъпките стават int
#     elif command_info[0] == 'shoot':  # проверяваме дали командата е shoot
#         target_down_pos = shoot(command_info[1])  # извикваме функцията shoot, параметър е посоката
#
#         if target_down_pos:  # проверяваме дали сме свалили мишена
#             targets_hit_positions.append(target_down_pos)  # добавяме позицията на свалената мишена
#             targets_hit += 1  # увеличаваме броя на свалените мишени с 1
#
#         if targets_hit == targets:  # проверяваме дали всички мишени са свалени
#             print(f'Training completed! All {targets} targets hit.')  # принтираме, че успешно сме завършили обучението
#             break  # прекратяваме цикъла
#
# if targets_hit < targets:  # проверяваме дали са останали мишени
#     print(f'Training not completed! {targets - targets_hit} targets left.')  # принтираме неуспешно завършено обучение
#
# [print(target_pos) for target_pos in targets_hit_positions]  # принтираме позициите на свалените мишени
