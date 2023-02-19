from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))


healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}
created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}
result = []
while textiles and medicaments:

    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()
    elements_sum = curr_textile + curr_medicament

    if elements_sum == 30:
        created_items["Patch"] += 1
    elif elements_sum == 40:
        created_items["Bandage"] += 1
    elif elements_sum == 100:
        created_items["MedKit"] += 1
    elif elements_sum > 100:
        created_items["MedKit"] += 1
        medicaments[-1] += elements_sum - 100
    else:
        medicaments.append(curr_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_data = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
for data in sorted_data:
    if int(data[1]) > 0:
        print(f"{data[0]} - {data[1]}")
if medicaments:
    for el in range(len(medicaments) - 1, -1, -1):
        result.append(medicaments[el])

    print(f"Medicaments left: {', '.join(str(el) for el in result)}")
elif textiles:
    print(f"Textiles left: {', '.join(str(el) for el in textiles)}")
