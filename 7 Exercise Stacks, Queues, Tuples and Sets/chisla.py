set_one = set(int(number) for number in input().split())
set_two = set(int(number) for number in input().split())

function = {
    "Add First": lambda x: [set_one.add(el) for el in x],
    "Add Second": lambda x: [set_two.add(el) for el in x],
    "Remove First": lambda x: [set_one.discard(el) for el in x],
    "Remove Second": lambda x: [set_two.discard(el) for el in x],
    "Check Subset": lambda: print(True) if set_one.issubset(set_two) or set_two.issubset(set_one) else print(False),
    }
for _ in range(int(input())):

    first_command, *data = input().split()

    command = first_command + ' ' + data.pop(0)

    if data:
        function[command](int(n) for n in data)
    else:
        function[command]()

print(*sorted(set_one), sep=', ')
print(*sorted(set_two), sep=', ')
# print(', '.join([str(n) for n in set_one]))
# print(', '.join([str(n) for n in set_two]))
