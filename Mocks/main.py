import requests

def api_call(url:str):
    response = requests.get(url)
    return {"data": response.json()}