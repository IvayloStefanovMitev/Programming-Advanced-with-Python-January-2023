from collections import deque


def people_queue():

    people = deque()
    while True:
        names = input()
        if names == COMMAND_START:
            break
        people.append(names)

    return people


COMMAND_END = 'End'
COMMAND_REFILL = 'refill'
COMMAND_START = 'Start'

quantity_of_water = int(input())


people_to_add = people_queue()

while True:

    command = input()

    if command == COMMAND_END:
        print(f"{quantity_of_water} liters left")
        break
    elif command.startswith(COMMAND_REFILL):
        split_command = command.split(' ')
        water_to_refill = split_command[1]
        quantity_of_water += int(water_to_refill)

    else:
        liters = int(command)

        if quantity_of_water >= liters:
            curr_person = people_to_add.popleft()
            quantity_of_water -= liters
            print(f"{curr_person} got water")
        else:
            curr_person = people_to_add.popleft()
            print(f"{curr_person} must wait")