class weather:


    def weather_check(self,temp:float):
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

    def rain_check(self, rain_chance:float):
        if rain_chance > 0.5:
            return "It's likely to rain today. Don't forget your umbrella!"
        elif rain_chance > 0.2:
            return "There's a slight chance of rain today. You might want to carry an umbrella just in case."
        elif rain_chance > 0.1:
            return "It's unlikely to rain today, but you might want to keep an eye on the weather just in case."
        else:
            return "It's not expected to rain today. Enjoy the sunshine!"


    def divide(self, a: float, b: float):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b