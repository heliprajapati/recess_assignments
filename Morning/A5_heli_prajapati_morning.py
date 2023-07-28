#Inheritance
#Exercise1
#Demostrate using inheritance to calculate area and perimeter of circle and rectangle 
"""
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create an instance of Circle
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

# Create an instance of Rectangle
rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
"""
"""

#Multiple inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        pass

class Convertible:
    def open_roof(self):
        pass

class SportsCar(Vehicle, Convertible):
    def drive(self):
        return "Vroom!"

    def open_roof(self):
        return "Opening the roof!"

class SUV(Vehicle):
    def drive(self):
        return "Rumbling!"

#Instances of the classes
sports_car = SportsCar("Ferrari")
suv = SUV("Toyota")

#Calling the methods
print(sports_car.brand)
print(sports_car.drive())
print(sports_car.open_roof())
print(suv.brand)
print(suv.drive())
"""

#Polymorphism
"""
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create instances of the classes
rectangle = Rectangle(5, 3)
circle = Circle(7)

# Call the methods
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
"""

"""
#overloading functions
class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    def add(self, *args):
        return sum(args)

#Create an instance of Calculator
calc = Calculator()

#Calling add() method with different arguments
print(calc.add(2, 3))            # Output: 5
print(calc.add(2, 3, 4))         # Output: 9
print(calc.add(2, 3, 4, 5))      # Output: 14
"""

# Abstraction
#Allow you to focus on essential features and hide them from unecessary details
#Example: Demostrate abstractions
"""
from abc import ABC, abstractmethod
class Vechicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(Vechicle):
    def start(self):
        print("starting the car")
    
    def stop(self):
        print("stopping the car")

class truck(Vechicle):
    def start(self):
        print("starting truck")

    def stop(self):
        print("stopping truck")

c1 = car()
t1 = truck()
c1.start()
t1.start()    
"""

#Exercise2: Demonstrate abstraction using calculating area of circle and rectangle
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Area of the circle:", circle.calculate_area())       # Output: 78.5
print("Area of the rectangle:", rectangle.calculate_area()) # Output: 24
"""
#A1_heli_prajapati_morning_py
#Assignment 1: Deadline 1st july 
#Create a receipt printing program with GUI interface
#Creating a hospital billing receipt
#The user should be able to enter his/her personal information like name, Doctor's name and amount to be paid

import tkinter as tk
from tkinter import messagebox

def print_receipt():
    # Get input values from the entry fields
    patient_name = name_entry.get()
    doctor_name = doctor_entry.get()
    amount_paid = float(amount_entry.get())

    # Perform receipt printing operations
    # ...

    # Display a message box with the receipt details
    receipt_message = f"Patient Name: {patient_name}\nDoctor Name: {doctor_name}\nAmount Paid: {amount_paid}"
    tk.messagebox.showinfo("Receipt", receipt_message)

    # Show the receipt message in a message box
    messagebox.showinfo("Receipt", receipt_message)

# Create the main window
window = tk.Tk()
window.title("Hospital Receipt")

# Create labels and entry fields for input
name_label = tk.Label(window, text="Patient Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

doctor_label = tk.Label(window, text="Doctor Name:")
doctor_label.pack()
doctor_entry = tk.Entry(window)
doctor_entry.pack()

amount_label = tk.Label(window, text="Amount Paid:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

# Create a button to print the receipt
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Start the GUI event loop
window.mainloop()
