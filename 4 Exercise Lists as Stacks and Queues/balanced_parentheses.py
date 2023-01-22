sequence_of_parentheses = input()

open_parentheses = []
for parentheses in sequence_of_parentheses:

    if parentheses in '{[(':
        open_parentheses.append(parentheses)
    elif not open_parentheses:
        print('NO')
        break
    elif open_parentheses.pop() + parentheses not in '{}[]()':
        print('NO')
        break

else:
    print('YES')