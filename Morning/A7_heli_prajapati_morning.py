# 1a) Show a context manager for file handling that automatically opens and closes a file.
#we use the with statement
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("heli.txt", "w") as file:
    file.write("I am heli prajapati")

# b) Shows a context manager for managing a database connection.
import sqlite3
def connect_db():
    #Connect to the database
    connection = sqlite3.connect('database.sqlite')
    return connection
def close_db(connection):
    #Close the database connection
    connection.close()
def with_db():
    #Context manager for managing a database connection
    connection = connect_db()
    try:
        yield connection
    finally:
        close_db(connection)

# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import threading
import time
def function_1():
    for i in range(5):
        print(f"Function 1: {i}")
        time.sleep(1)
def function_2():
    for i in range(5):
        print(f"Function 2: {i}")
        time.sleep(2)
if __name__ == "__main__":
    # Create two threads
    thread_1 = threading.Thread(target=function_1)
    thread_2 = threading.Thread(target=function_2)
    # Start the threads
    thread_1.start()
    thread_2.start()
    # Wait for the threads to finish
    thread_1.join()
    thread_2.join()