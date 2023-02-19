def multiply(*args):
    start_multiply = 1
    for number in args:
        start_multiply *= number
    return start_multiply


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
