from collections import deque

names = input().split(' ')
toss = int(input())
people = deque(names)
while len(people) > 1:
    for person in range(toss - 1):
        people.append(people.popleft())
    person_left = people.popleft()
    print(f"Removed {person_left}")
print(f"Last is {people[0]}")