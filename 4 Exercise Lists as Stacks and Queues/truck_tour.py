from collections import deque
pump_counter = 0
petrol_counter = 0


pump_data = deque([[int(data) for data in input().split()] for _ in range(int(input()))])

pump_data_copy = pump_data.copy()

while pump_data_copy:
    petrol, distance = pump_data_copy.popleft()

    petrol_counter += petrol

    if petrol_counter - distance < 0:
        pump_data.rotate(-1)
        pump_data_copy = pump_data.copy()
        petrol_counter = 0
        pump_counter += 1
    else:

        petrol_counter -= distance


print(pump_counter)