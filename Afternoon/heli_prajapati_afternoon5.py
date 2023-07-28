#Exception handling
#Exception handling (try, except, finally and raise)
try:
    x = 10
    y = 0
    z = x/y #Zero division error occurs here
    print(z)
except ZeroDivisionError:
    print('Error:division by zero')
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print('This is always executed')

#Raising an Exception:
#Means creating and triggering an exception during the execution of your code. 
#The raise statement allows the programmer to force a specified exception to occur.
try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise ValueError("Number must be positive.")
    print("Number entered:", x)
except ValueError as ve:
    print("Error:", str(ve))

# #User-defined exception
# class SalaryNotInRangeError(Exception):
# #Exception raised for errors in the input salary.
#     def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)

# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)


#File handling
#File handling in Python allows you to read from and write to files on your computer.
#file handling operations in Python:

# #1. Reading from a File:
# # Opening the file in read mode
# file = open("heli.txt", "r")
# # Reading the entire contents of the file
# content = file.read()
# # Printing the contents
# print(content)
# # Closing the file
# file.close()

# #2. Writing to a File:
# # Opening the file in write mode
# file = open("heli.txt", "w")
# # Writing content to the file
# file.write("My name is heli")
# # Closing the file
# file.close()

# #3. Appending to a File:
# # Open the file in append mode
# file = open("heli.txt", "a")
# # Append content to the file
# file.write("\nI am in bsse")
# # Close the file
# file.close()

# #4. Reading Line by Line:
# # Open the file in read mode
# file = open("heli.txt", "r")
# # Read the file line by line
# for line in file:
#     print(line)
# # Close the file
# file.close()

# #5. Handling Exceptions:
# # Open the file in read mode
# try:
#     file = open("hell.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     # Close the file in the finally block to ensure it's always closed
#     file.close()

#User Registration System
def register_user():
    # Get user details
    name = input("Enter name: ")
    email = input("Enter email: ")

    # Open file in append mode
    with open("users.txt", "a") as file:
        # Write user details to the file
        file.write(f"{name},{email}\n")
    
    print("User registered successfully!")

def display_users():
    # Open file in read mode
    with open("users.txt", "r") as file:
        # Read and display each user from the file
        for line in file:
            name, email = line.strip().split(",")
            print(f"Name: {name}\tEmail: {email}")
 
def main():
    while True:
        print("1. Register User")
        print("2. Display Users")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





