def santa_func(matrix_data, number_of_presents):
    current_presents = number_of_presents
    kids_got_present = 0
    nice_kids = 0
    nice_kids_left = 0
    santa_pos = []
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == 'S':
                santa_pos = [row, col]
                matrix_data[row][col] = '-'
                break

    for row in range(len(matrix_data)):
        if 'V' in matrix_data[row]:
            nice_kids += matrix_data[row].count('V')

    while current_presents > 0:

        direction = input()

        if direction == 'Christmas morning':
            break

        santa_pos_row = santa_pos[0] + directions[direction][0]
        santa_pos_col = santa_pos[1] + directions[direction][1]

        if 0 <= santa_pos_row < len(matrix_data) and 0 <= santa_pos_col < len(matrix_data):

            santa_pos = [santa_pos_row, santa_pos_col]

            if matrix_data[santa_pos_row][santa_pos_col] == 'V':
                current_presents -= 1
                kids_got_present += 1
                nice_kids_left += 1
                matrix_data[santa_pos_row][santa_pos_col] = '-'

            elif matrix_data[santa_pos_row][santa_pos_col] == 'X':
                matrix_data[santa_pos_row][santa_pos_col] = '-'

            elif matrix_data[santa_pos_row][santa_pos_col] == 'C':

                for curr_direction, position in directions.items():
                    santa_pos_row_cookie = santa_pos_row + position[0]
                    santa_pos_col_cookie = santa_pos_col + position[1]

                    if current_presents <= 0:
                        break

                    if matrix_data[santa_pos_row_cookie][santa_pos_col_cookie] == 'V':
                        current_presents -= 1
                        kids_got_present += 1
                        nice_kids_left += 1
                        matrix_data[santa_pos_row_cookie][santa_pos_col_cookie] = '-'
                    elif matrix_data[santa_pos_row_cookie][santa_pos_col_cookie] == 'X':
                        current_presents -= 1
                        kids_got_present += 1
                        matrix_data[santa_pos_row_cookie][santa_pos_col_cookie] = '-'


            # if current_presents < 0:
            #
            #     break

    matrix_data[santa_pos[0]][santa_pos[1]] = 'S'

    if current_presents <= 0:
        print('Santa ran out of presents!')
    print(*[' '.join(line) for line in matrix_data], sep='\n')
    if nice_kids == nice_kids_left:
        print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
    elif nice_kids > nice_kids_left:
        print(f'No presents for {nice_kids - nice_kids_left} nice kid/s.')


def matrix_func():
    present = int(input())
    size = int(input())
    curr_matrix = []
    for row in range(size):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix, present


matrix, presents = matrix_func()

santa_func(matrix, presents)