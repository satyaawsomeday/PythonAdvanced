import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url:str):
    print(f"Fetching data from {url}")
    # wait_time = 5
    # time.sleep(wait_time)
    print(f"Data fetched from {url}")
    return f"Data from {url}"

urls_list = ["https://api.example1.com", 
             "https://api.example2.com", 
             "https://api.example3.com",
             "https://api.example4.com",
             "https://api.example5.com"]

# for url in urls_list:
#     fetch_data(url)

results = []
with ThreadPoolExecutor(len(urls_list)) as executor:
    futures = executor.map(fetch_data, urls_list)
    results.extend(futures)

print("Results:", results)