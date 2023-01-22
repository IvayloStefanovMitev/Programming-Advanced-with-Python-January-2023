def diagonal_difference(primary, secondary):
    difference = abs(primary - secondary)

    print(difference)


def sum_of_secondary_diagonal(matrix_data):
    matrix_size = len(matrix_data)
    secondary_diagonal = [matrix_data[r][matrix_size - 1 - r] for r in range(matrix_size - 1, - 1, - 1)]

    return secondary_diagonal


def sum_of_primary_diagonal(matrix_data):
    matrix_size = len(matrix_data)
    primary_diagonal = [matrix_data[r][r]for r in range(matrix_size)]

    return primary_diagonal


def matrix_func():
    rows = int(input())
    curr_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split()))
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
primary_sum = sum(sum_of_primary_diagonal(matrix))
secondary_sum = sum(sum_of_secondary_diagonal(matrix))
diagonal_difference(primary_sum, secondary_sum)