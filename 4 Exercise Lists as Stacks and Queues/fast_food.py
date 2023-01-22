from collections import deque

quantity_food = int(input())

order_deque = deque([int(number) for number in input().split()])

print(max(order_deque))

for order in order_deque.copy():
    if quantity_food - order >= 0:
        order_deque.popleft()
        quantity_food -= order
    else:
        print(f"Orders left: {' '.join(str(left_order) for left_order in order_deque)}")
        break
else:
    print("Orders complete")