from collections import deque

seats = input().split(", ")
first_nums = deque(map(int, input().split(", ")))
second_nums = deque(map(int, input().split(", ")))

rotation_counter = 0

matched_seats = []

while rotation_counter < 10 and len(matched_seats) < 3:

    first = first_nums.popleft()
    second = second_nums.pop()

    sum_of_nums = first + second
    letter = chr(sum_of_nums)
    created_seat = [str(first) + letter, str(second) + letter]

    for seat in created_seat:
        if seat in matched_seats:
            break
        if seat in seats:
            matched_seats.append(seat)
            seats.remove(seat)
            break
        else:
            first_nums.append(first)
            second_nums.appendleft(second)
    rotation_counter += 1
print(f"Seat matches: {', '.join(curr_seat for curr_seat in matched_seats)}")
print(f"Rotations count: {rotation_counter}")

# from collections import deque
#
# seats = input().split(", ")
# first_nums = deque(map(int, input().split(", ")))
# second_nums = deque(map(int, input().split(", ")))
#
# rotation_counter = 0
# seats_matched_counter = 0
# matched_seats = []
#
# while rotation_counter < 10 and seats_matched_counter < 3:
#
#     first = first_nums.popleft()
#     second = second_nums.pop()
#
#     sum_of_nums = first + second
#     letter = chr(sum_of_nums)
#     created_seat = [str(first) + letter, str(second) + letter]
#
#     if created_seat[0] in seats:
#         seats_matched_counter += 1
#         if created_seat[0] in matched_seats:
#             continue
#         matched_seats.append(created_seat[0])
#     elif created_seat[1] in seats:
#         seats_matched_counter += 1
#         if created_seat[1] in matched_seats:
#             continue
#         matched_seats.append(created_seat[1])
#
#     else:
#         first_nums.append(first)
#         second_nums.appendleft(second)
#
#     rotation_counter += 1
#
# print(f"Seat matches: {', '.join(curr_seat for curr_seat in matched_seats)}")
# print(f"Rotations count: {rotation_counter}")