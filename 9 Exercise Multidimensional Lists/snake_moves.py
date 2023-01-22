from collections import deque


def matrix_func():
    rows, cols = map(int, input().split())

    word = list(input())

    word_copy = deque(word)
    for row in range(rows):
        while len(word_copy) < cols:
            word_copy.extend(word)

        if row % 2 == 0:
            for col in range(cols):
                print(word_copy.popleft(), end='')
            print()
        else:
            print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')


matrix_func()
