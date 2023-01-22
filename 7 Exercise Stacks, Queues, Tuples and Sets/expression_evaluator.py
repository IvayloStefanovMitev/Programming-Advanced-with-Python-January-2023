from functools import reduce

expression = input().split()

index = 0
expression_func = {
    "*": lambda x: reduce(lambda a, b: int(a) * int(b), expression[:index]),
    "/": lambda x: reduce(lambda a, b: int(a) / int(b), expression[:index]),
    "-": lambda x: reduce(lambda a, b: int(a) - int(b), expression[:index]),
    "+": lambda x: reduce(lambda a, b: int(a) + int(b), expression[:index]),
}
for el in expression.copy():

    if el in '*/+-':
        result = expression_func[el](index)
        [expression.pop(1) for i in range(index)]
        expression[0] = result
        index = 0

    index += 1
print(int(expression[0]))