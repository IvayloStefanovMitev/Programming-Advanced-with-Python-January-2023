def grocery_store(**kwargs):
    return "\n".join([f"{product}: {quantity}" for product, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))])

    # sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # result = []
    # for product, quantity in sorted_data:
    #     result.append(f"{product}: {quantity}")
    # return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
