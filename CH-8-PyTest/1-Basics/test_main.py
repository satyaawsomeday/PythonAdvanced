from main  import weather_check

def test_weather_check():
    assert weather_check(-5) == "It's freezing outside"
    assert weather_check(25) == "It's cloudy outside"
    assert weather_check(35) == "It's hot outside."

if __name__ == "__main__":
    test_weather_check()
    print("All tests passed!")
