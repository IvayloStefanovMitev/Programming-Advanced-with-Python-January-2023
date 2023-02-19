# def numbers_func(positive_negative):
#     negative_numbers = []
#     positive_numbers = []
#     for number in positive_negative:
#         if int(number) < 0:
#             negative_numbers.append(int(number))
#         elif int(number) > 0:
#             positive_numbers.append(int(number))
#     print(sum(negative_numbers))
#     print(sum(positive_numbers))
#     if abs(sum(negative_numbers)) > sum(positive_numbers):
#         print("The negatives are stronger than the positives")
#     else:
#         print("The positives are stronger than the negatives")
#
#
# numbers = input().split()
# numbers_func(numbers)
#
#
def positive_func():
    sum_numbers = 0

    for num in numbers:
        if num > 0:
            sum_numbers += num

    return sum_numbers


def negative_func():
    sum_numbers = 0

    for num in numbers:
        if num < 0:
            sum_numbers += num

    return sum_numbers


numbers = [int(number) for number in input().split()]

positive_numbers = positive_func()
negative_numbers = negative_func()

print(negative_numbers)
print(positive_numbers)
if abs(negative_numbers) > positive_numbers:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")