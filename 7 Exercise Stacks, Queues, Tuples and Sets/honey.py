from collections import deque

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())
nectar_counter = 0

nectar_collected_func = {
    "+": lambda a, b: int(a) + int(b),
    "-": lambda a, b: int(a) - int(b),
    "*": lambda a, b: int(a) * int(b),
    "/": lambda a, b: int(a) / int(b),
}

while bees and nectar:
    bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar > bee:
        result = nectar_collected_func[symbols.popleft()](bee, curr_nectar)
        nectar_counter += abs(result)
    elif curr_nectar < bee:
        bees.appendleft(bee)
        continue

print(f"Total honey made: {nectar_counter}")
if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(curr_nectar) for curr_nectar in nectar)}")
