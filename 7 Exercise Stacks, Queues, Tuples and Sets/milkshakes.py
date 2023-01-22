from collections import deque

chocolates = deque(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()
    if milk <= 0 and chocolate <= 0:
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk == chocolate:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(chocolate) for chocolate in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(cup) for cup in cups_of_milk)}")
else:
    print("Milk: empty")

