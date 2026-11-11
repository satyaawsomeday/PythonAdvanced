def my_decorator(fx):
    def mainfunc(*args):
        print("Before calling the function")
        response = fx(*args)
        print("After calling the function")
        return response
    return mainfunc

@my_decorator
def fetch_data(url:str, path:str):
    return f"Fetching data from {url} saving to {path}"

obj = fetch_data("https://api.example.com", "/data/output.json")
print(obj)