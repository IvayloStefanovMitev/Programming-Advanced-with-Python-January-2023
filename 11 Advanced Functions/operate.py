from operator import sub
from functools import reduce


def operate(operator, *args):
    if operator == '*':
        start_multiply = 1
        for number in args:
            start_multiply *= number
        return start_multiply
    elif operator == '/':
        start_divide = args[0]
        for number in args[1:]:
            if number == 0:
                continue
            start_divide /= number
        return start_divide

    elif operator == '+':
        start_additions = 0
        for number in args:
            start_additions += number
        return start_additions
    elif operator == '-':
        return reduce(sub, args)


print(operate("/", 6, 2, 0))