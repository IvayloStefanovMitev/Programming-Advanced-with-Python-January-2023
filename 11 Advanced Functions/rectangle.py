def rectangle(length, width):
    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return 2 * (length + width)

    if type(length) is not int or type(width) is not int:
        return "Enter valid values!"

    return f"""Rectangle area: {rectangle_area()}
Rectangle perimeter: {rectangle_perimeter()}"""


print(rectangle('2', 10))

