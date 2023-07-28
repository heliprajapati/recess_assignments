#OOP
#key concepts
"""
1.class
2.object
3.encapsulation
4.inheritance
5.polymorphism
6.abstraction

"""
#class
# Example1: car
"""
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def start_engine(self):
        print("started")
    def stop_engine(self):
        print("stopped")
        
#Object
#An object is an instance of class which has its own state and behavior
#example 
my_car = Car("tesla", 2022)
print(my_car.year)
print(my_car.model)
my_car.start_engine()
"""



#Encapsulation
#key main goals of encapsulation are 
"""
- to hide implementation details from users/clients;
- to prevent unauthorized access or modification by other objects that use it
- Code organization and modularity 
"""
#Example with a bank account
"""
class BaankAcoount:
    def __init__(self, account_num, balance):
        self._account_number = account_num #encapsulates the account number
        self._balance = balance # encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount

    def withdrawal(self,amount):
        if (self._balance >= amount):
            self._balance-=amount
        else:
            print("Insufficient funds")

    def displ_balance(self):
        return self._balance
#create a bank object 
my_account=BaankAcoount("123456789", 1000)
#access the bank object and modify encapsulated attributes indirectly
print( my_account. _account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdrawal(100)
print(my_account._balance)
"""
#Exercise 1: create an employee class with methods for calculating bonus(15)
"""
class Employee:
    def __init__ (self, salary):
        self.salary = salary

    def salary_cal(self):
        bonus = 0.15 * self.salary
        print("Employee bonus is: ", bonus)

E1 = Employee (2000)
E2 = Employee (3500)
E1.salary_cal()
E2.salary_cal()
"""

#Exercise 2: convert temperature(37 celsius) celsius to fahrenheit
"""
class TemperatureCon:
    def __init__(self):
        self.temp_converter()
    def temp_converter(self):
        while True:
            _celsius = input ("Enter temperature in Celsius or no to quit:")
            if _celsius.lower() == 'no':
                break
            _celsius = float (_celsius)
            fahrenheit = (_celsius * 9/5) + 32
            print(f"{_celsius}°C = {fahrenheit}°F")
"""


#Assignment 1: show encapsulation with employee information to give a pay increamentation(salary with employee infor to new_salary)
#eg, from 850000 to 1000000
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def increase_pay(self, increment):
        self._salary += increment

    def display_info(self):
        print("Employee Name:", self._name)
        print("Current Salary:", self._salary)

# Creating an object
E1 = Employee("heli", 850000)
#employee information before the increment
E1.display_info()
increment = 150000
E1.increase_pay(increment)
#employee information after the increment
E1.display_info()

































