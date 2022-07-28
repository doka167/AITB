#1.1

from cmath import pi
from unicodedata import name

class Circle:
    def __init__(self , raduis , color):
        self.raduis = raduis
        self.color = color

    def getRaduis(self):
        return self.raduis

    def getColor(self):
        return self.color

    def setRaduis(self , raduis):
        self.raduis = raduis
    
    def setColor(self , color):
        self.color = color
    
    def getArea(self):
        return pow(self.raduis , 2) * pi

    def getCircumference(self):
        return 2 * pi * self.raduis

    def __str__(self):
        return f"Raduis = {self.raduis} \n color = {self.color} \n Area = {self.getArea()} \n Circumfernce = {self.getCircumference()}"

circle1 = Circle(4, "red")
print(circle1)

print('-------------------------------------------------------------------------------------------------------')
#1.3

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def getWidth(self) :
        return self.width

    def setLength(self , length):
        self.length = length
    
    def setWidth(self, width):
        self.width = width

    def getArea(self):
        return (self.width * self.length)
    
    def getPerimeter(self):
        return (2 * self.length * self.width)

    def __str__(self) :
        return f"Length = {self.length} \n Width = {self.width} \n Area = {self.getArea()} \n Perimeter = {self.getPerimeter()}"

rect = Rectangle(2,4)
print(rect)

print('-------------------------------------------------------------------------------------------------------')
#1.4

class Employee:
    def __init__(self , id ,firstName , secondName , salary) :
        self.id = id
        self.firstName = firstName
        self.secondName = secondName
        self.salary = salary

    def getId(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getSecondName(self):
        return self.secondName

    def getName(self):
        return self.firstName + " " + self.secondName
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self , salary):
        self.salary = salary
    
    def getAnnualSalary(self):
        return (self.salary * 12)

    def raiseSalary(self , percent):
        self.salary= (self.salary * percent / 100) + self.salary
        return self.salary

    def __str__(self):
        return f"Employee id : {self.id} \n Name: {self.getName()} \n Salary: {self.salary}"        

E1 = Employee(16767 , 'Mohamed' , 'Khalid' , 35000)
print(f"Annual Salary : {E1.getAnnualSalary()}")
print(E1)

E1.raiseSalary(5)
print(E1)

print('-------------------------------------------------------------------------------------------------------')
#1.6

class Account:
    def __init__(self , id , name , balance):
        self.id = id
        self.name = name
        self.balance = balance
    
    def getId(self):
        return self. id
    
    def getName(self):
        return self.name
    
    def getBalance(self):
        return self.balance

    def credit(self, amount):
        self.balance = self.balance +amount
        print(f'Balance Updated ! your current balance is {self.balance}')
        return f"Current balance is {self.balance}"
    
    def debit(self,amount):
        if amount <= self.balance :
            self.balance = self.balance - amount
            print(f'Balance Updated ! your current balance is {self.balance}')
        else:
            print('Amount Exceeded Balance \n')
        return f"Current balance is {self.balance}"

    def transfereTo(self , Account, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            Account.credit(amount)
            print(f'Transfere Completed and your current balance is {self.balance}')
        else:
            print('Amount Exceeded Balance \n')
        return f"Current balance is {self.balance}"

    def __str__(self) -> str:
        return f"Account Id : {self.id} \n Name: {self.name} \n Balance: {self.balance}"

a1 = Account(1 , 'Mohamed' , 50000)
a2 = Account(1 , 'Ahmed' , 20000)

a1.credit(50000)
a2.debit(10000)

a1.transfereTo(a2,40000)

print(a1)
print(a2)