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

async def api_call():
    await asyncio.sleep(3)
    return "Orders data from API"

async def execute():
    print("Executing API call...")
    result = await api_call() #thread will be released to other tasks while waiting for the API response
    print("Data received:", result)

asyncio.run(execute())