from collections import deque

milligrams_caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

stamat_caffeine = 0
max_caffeine = 300

while milligrams_caffeine and energy_drinks:

    caffeine = milligrams_caffeine.pop()
    drinks = energy_drinks.popleft()

    if (drinks * caffeine) + stamat_caffeine <= max_caffeine:
        stamat_caffeine += drinks * caffeine

    elif (drinks * caffeine) + stamat_caffeine > max_caffeine:
        energy_drinks.append(drinks)
        if stamat_caffeine - 30 >= 0:

            stamat_caffeine -= 30
        else:
            stamat_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(str(drink) for drink in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")