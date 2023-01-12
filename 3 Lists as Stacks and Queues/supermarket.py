from collections import deque

names_deque = deque()

COMMAND_END = 'End'
COMMAND_PAID = 'Paid'

while True:
    names = input()

    if names == COMMAND_END:
        print(f"{len(names_deque)} people remaining.")
        break

    elif names == COMMAND_PAID:
        while names_deque:
            people_on_the_queue = names_deque.popleft()
            print(people_on_the_queue)

    else:
        names_deque.append(names)
