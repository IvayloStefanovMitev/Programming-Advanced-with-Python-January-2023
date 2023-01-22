number = int(input())
elements = set()

for _ in range(number):
    for el in input().split():
      elements.add(el)

print(*elements, sep='\n')
