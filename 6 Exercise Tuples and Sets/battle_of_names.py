even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):

    ascii_sum = (sum([ord(letter) for letter in input()])) // row

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

if sum(even_set) == sum(odd_set):
    print(', '.join(str(numbers) for numbers in even_set.union(odd_set)))
elif sum(odd_set) > sum(even_set):
    print(', '.join(str(numbers) for numbers in odd_set.difference(even_set)))
elif sum(odd_set) < sum(even_set):
    print(', '.join(str(numbers) for numbers in even_set.symmetric_difference(odd_set)))
