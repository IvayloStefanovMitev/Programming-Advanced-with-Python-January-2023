data = input().split('|')
result = []
for el in data[::-1]:
    result.extend(el.split())

print(*result)