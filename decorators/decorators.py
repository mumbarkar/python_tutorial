import time

def timer(func):
    
    def wrapper():
        
        start = time.time()
        
        func()
        
        end = time.time()
        
        print(f"Execution time for {func.__name__}: {end - start:.4f} seconds")
        
    return wrapper

@timer
def process():
    time.sleep(2)
    print("Processing...")
    
process()