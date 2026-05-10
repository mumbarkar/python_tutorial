# loading the asyncio module
import asyncio

# defining an asynchronous coroutine
async def fetch_data(id, delay):
    print(f"Fetching data for ID: {id} with a delay of {delay} seconds...")
    
    await asyncio.sleep(delay)  # simulating a delay
    
    print(f"Data for ID: {id} fetched successfully!")
     
    return f"Data for ID: {id} fetched after {delay} seconds!"
    
async def main():
    # create tasks for running coroutines concurently
    task1 = asyncio.create_task(fetch_data(1,5))
    task2 = asyncio.create_task(fetch_data(2,10))
    task3 = asyncio.create_task(fetch_data(3,15))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, result2, result3)
    
if __name__ == '__main__':
    asyncio.run(main())