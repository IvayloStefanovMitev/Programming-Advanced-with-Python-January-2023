n, m = [int(sets) for sets in input().split()]

first_set = set(int(input()) for _ in range(n))
second_set = set(int(input()) for _ in range(m))

unique = first_set.intersection(second_set)

print(*unique, sep='\n')