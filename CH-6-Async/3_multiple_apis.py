# Normal synchronous API call simulation
# import time

# def api_call():
#     time.sleep(3)
#     return "Orders data from API"

# def execute():
#     print("Executing API call...")
#     result = api_call()
#     print("Data received:", result)

# execute()

# Asynchronous API call simulation
import asyncio

async def api_call(url:str,wait_time:int):
    print("Fetching data from API...")
    await asyncio.sleep(wait_time) #thread will be released to other tasks while waiting for the API response
    print(f"Data received from {url}")
    return f"Orders data from {url}"

async def main():
    #creatuing tasks with gather to run multiple API calls concurrently
    tasks=await asyncio.gather(
        api_call("https://api1.com", 2), 
        api_call("https://api2.com", 1), 
        api_call("https://api3.com", 3))
    
    # Another way to create tasks using list comprehension
    # tasks=[api_call(url) for url in ["https://api1.com", "https://api2.com", "https://api3.com"]]
    # results=await asyncio.gather(*tasks)

asyncio.run(main())