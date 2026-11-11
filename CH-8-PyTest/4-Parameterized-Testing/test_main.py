from main  import weather_check
import pytest

@pytest.mark.parametrize("temp, expected", [
    (-5, "It's freezing outside"),
    (25, "It's cloudy outside"),
    (35, "It's hot outside.")
])

def test_weather_check(temp, expected):
    assert weather_check(temp) == expected

if __name__ == "__main__":
    test_weather_check()
    print("All tests passed!")
