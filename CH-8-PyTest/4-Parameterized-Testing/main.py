def weather_check(temp:float):
    if temp < 0:
        return "It's freezing outside"
    elif temp < 15:
        return "It's cold Outside."
    elif temp < 25:
        return "It's pleasant Outside."
    elif temp > 30:
        return "It's hot outside."
    else:
        return "It's cloudy outside"

