def forecast(*args):

    weather_in_order = {
        'Sunny': 1,
        'Cloudy': 2,
        'Rainy': 3,
    }

    weather_dictionary = {}
    weather_cities = {}
    for data in args:
        weather_dictionary[data[0]] = weather_in_order[data[1]]
        weather_cities[data[0]] = data[1]

    sorted_weather = dict(sorted(weather_dictionary.items(), key=lambda x: (x[1], x[0])))
    result = []
    for city in sorted_weather.keys():
        result.append(f'{city} - {weather_cities[city]}')

    return '\n'.join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))




