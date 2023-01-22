numbers = [int(n) for n in input().split()]
# numbers.reverse()
# print(*numbers)
while numbers:
    print(numbers.pop(), end=' ')