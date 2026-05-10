# load python module or libraries
import asyncio

# defining an asynchronous coroutine function to fetch data with a delay
async def fetch_data(id, delay):
    print(f"Fetching data for ID: {id} with a delay of {delay} seconds...")
    
    await asyncio.sleep(delay)  # simulating a delay
    
    print(f"Data for ID: {id} fetched successfully!")
     
    return f"Data for ID: {id} fetched after {delay} seconds!"

# schedule multiple coroutines to run concurrently and gather their results 
async def main():
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 5),
        fetch_data(3, 2)
    )
    
    # Results are returned in the order they were passed to gather()
    print(f"Results: {results}")

# run the main function using asyncio's event loop
if __name__ == '__main__':
    asyncio.run(main())