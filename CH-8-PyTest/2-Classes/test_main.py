from main import weather

def test_weather_check():
    w = weather()
    assert w.weather_check(-5) == "It's freezing outside"
    assert w.weather_check(25) == "It's cloudy outside"
    assert w.weather_check(35) == "It's hot outside."

def test_rain_check():
    w = weather()
    assert w.rain_check(0.6) == "It's likely to rain today. Don't forget your umbrella!"
    assert w.rain_check(0.3) == "There's a slight chance of rain today. You might want to carry an umbrella just in case."
    assert w.rain_check(0.15) == "It's unlikely to rain today, but you might want to keep an eye on the weather just in case."
    assert w.rain_check(0.05) == "It's not expected to rain today. Enjoy the sunshine!"

if __name__ == "__main__":
    test_weather_check()
    test_rain_check()
    print("All tests passed!")
