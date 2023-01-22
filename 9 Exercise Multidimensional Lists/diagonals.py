def sum_of_secondary_diagonal(matrix_data):

    matrix_size = len(matrix_data)
    secondary_diagonal = [matrix_data[r][matrix_size - 1 - r] for r in range(matrix_size - 1, - 1, - 1)]

    print(f"Secondary diagonal: {', '.join([str(n) for n in secondary_diagonal][::-1])}.\
     Sum: {sum(secondary_diagonal)}")


def sum_of_primary_diagonal(matrix_data):
    matrix_size = len(matrix_data)
    primary_diagonal = [matrix_data[r][r] for r in range(matrix_size)]
    print(f"Primary diagonal: {', '.join([str(n) for n in primary_diagonal])}. Sum: {sum(primary_diagonal)}")


def matrix_func():
    rows = int(input())
    curr_matrix = []
    for row in range(rows):
        row_data = list(map(int, input().split(", ")))
        curr_matrix.append(row_data)
    return curr_matrix


matrix = matrix_func()
sum_of_primary_diagonal(matrix)
sum_of_secondary_diagonal(matrix)