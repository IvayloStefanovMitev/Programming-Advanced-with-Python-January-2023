box_of_cloths = [int(cloths) for cloths in input().split()]
rack_capacity = int(input())
curr_capacity = rack_capacity
rack_counter = 1

for cloth in box_of_cloths.copy():
    box_of_cloths.pop()
    if curr_capacity >= cloth:

        curr_capacity -= cloth

    else:
        curr_capacity = rack_capacity - cloth
        rack_counter += 1
print(rack_counter)
