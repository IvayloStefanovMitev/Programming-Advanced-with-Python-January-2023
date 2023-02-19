def even_odd(*args):
    command = args[-1]
    result = []

    for num in args[:-1]:
        if num % 2 == 0 and command == 'even':
           result.append(num)
        elif num % 2 == 1 and command == 'odd':
            result.append(num)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

