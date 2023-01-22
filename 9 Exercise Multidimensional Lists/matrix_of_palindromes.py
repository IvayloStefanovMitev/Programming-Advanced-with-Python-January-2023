def matrix_func():
    rows, cols = map(int, input().split())
    start_end = ord('a')

    for row in range(start_end, start_end + rows):
        for col in range(start_end, start_end + cols):
            print(f"{chr(row)}{chr(row + col - start_end)}{chr(row)}", end=' ')
        print()


matrix_func()