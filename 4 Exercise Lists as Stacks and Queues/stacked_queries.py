numbers = []

map_function = {

    1: lambda data: numbers.append(data[1]),
    2: lambda data: numbers.pop() if numbers else None,
    3: lambda data: print(max(numbers)) if numbers else None,
    4: lambda data: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    number_data = [int(data) for data in input().split()]
    map_function[number_data[0]](number_data)

numbers. reverse()
print(*numbers, sep=', ')