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
import time

# First task to simulate API call with a wait time
async def api_call(url:str,delay:int=3):
    print("Fetching data from API...")
    await asyncio.sleep(delay) #thread will be released to other tasks while waiting for the API response
    print(f"Data received from {url}")

# Second task to execute
async def execute():
    time.sleep(5) #thread will be blocked for 5 seconds while waiting for the API response
    print("Execution completed.")

# Third task
async def transformation():
    asyncio.sleep(2)
    print("Data transformation completed.")
    

async def main():
    #creatuing tasks with gather to run multiple API calls concurrently
    tasks=await asyncio.gather(
        api_call("https://api1.com"), 
        execute(),
        transformation())
    
    # Another way to create tasks using list comprehension
    # tasks=[api_call(url) for url in ["https://api1.com", "https://api2.com", "https://api3.com"]]
    # results=await asyncio.gather(*tasks)
    print("All tasks completed.")

asyncio.run(main())