def age_assignment(*args, **kwargs):

    result = []
    for key in kwargs:
        for name in args:
            if name.startswith(key):

                result.append(f"{name} is {kwargs[key]} years old.")

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))


# def age_assignment(*args, **kwargs):
#
#     result = []
#     for key, value in kwargs.items():
#         person_name = ""
#         for name in args:
#             if name.startswith(key):
#                 person_name = name
#                 break
#         result.append(f"{person_name} is {value} years old.")
#
#     return '\n'.join(sorted(result))
