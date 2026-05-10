from contextlib import contextmanager

@contextmanager
def database():
    
    print("Connecting to the database...")
    
    yield
    
    print("Closing the database connection...")