def shop_from_grocery_list(budged, list_of_products, *args):

    for data in args:
        product = data[0]
        price = data[1]
        if product in list_of_products:
            if budged >= price:
                list_of_products.remove(product)
                budged -= price
            else:
                break
        continue
    if not list_of_products:
        return f"Shopping is successful. Remaining budget: {budged:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(product for product in list_of_products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
