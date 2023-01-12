expression = input()
indexes = []

for i in range(len(expression)):
    char = expression[i]

    if char == '(':
        indexes.append(i)
    elif char == ')':
        last_index = indexes.pop()
        result = expression[last_index:i + 1]
        print(result)