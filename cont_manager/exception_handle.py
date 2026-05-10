class Database:
    
    def __enter__(self):
        print("Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnected")


with Database():
    print("Running query")

    raise ValueError("Something failed")