def square_matrix(matrix_data):
    rows = len(matrix_data)
    cols = len(matrix_data[0])
    biggest_matrix_data = []
    max_size = float('-inf')

    for row in range(rows - 2):
        for col in range(cols - 2):
            first_row = matrix_data[row][col:col + 3]
            second_row = matrix_data[row + 1][col:col + 3]
            third_row = matrix_data[row + 2][col:col + 3]
            sum_of_curr_matrix = sum(first_row) + sum(second_row) + sum(third_row)
            if sum_of_curr_matrix > max_size:
                max_size = sum_of_curr_matrix
                biggest_matrix_data.clear()
                biggest_matrix_data.append([first_row, second_row, third_row])

    print(f"Sum = {max_size}")
    for row in range(len(biggest_matrix_data)):
        for col in range(len(biggest_matrix_data[row])):
            print(*biggest_matrix_data[row][col], end=' ')
            print()


def matrix_func():
    rows, cols = map(int, input().split())
    curr_matrix = []

    for row in range(rows):
        row_data = list(map(int, input(). split()))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
square_matrix(matrix)

