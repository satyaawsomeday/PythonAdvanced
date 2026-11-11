from main import api_call
import pytest

def test_api_call(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.json.return_value = {"main": {"key": "value"}}

    result = api_call("https:openweathermap.org/data/2.5/weather?q=London&appid=1234567")
    assert result == {"data": {"main": {"key": "value"}}}
    