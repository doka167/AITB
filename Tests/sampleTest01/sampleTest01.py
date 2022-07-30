# Question 1 (Answer the following) :-
#######################################

'''
1- What are lists and tuples? What is the key difference between
the two?
    -> Lists and Tuples are data structure in python that can hold multiple items/values in single variable 
    -> The key difference between tuples and lists is that tuples are immutable (can not be modified),  while 
        lists are mutable (can be modified)


2- What is break, continue and pass in Python?
    -> break, continue and pass are loop control statments that affect the normal loop exectution sequence
    -> break :- end the loop immediatily when compiled
    -> continue :- end only the current iteration of the loop and start execute the next iteration
    -> pass :- it does nothing, used only as placeholder if ypu don't want to fill the place with code in the 
        mean time.

3- What is the use of self in Python?
    -> it referes to the current class items (instance of the class it is in), to differentiate between 
        the current class attributes and the passed to class attributes

4- What is docstring in Python?
    -> similar to comments, but defined with three double-quotes (such as this one the questin answered in),
    used to describe the use of the source code that it describes.
    -> used with classes,methods and models to let the programmers understand its funtionalities without 
        reading the code

5- Python supports multiple inheritance . explain it with example
    ->  Means that the class can have more than one parent to be derived from.
    -> The derived class will inherits all the parents classes methods and attributes
    -> Ex :-
        class Animal:
            def Hair(self):
                print ('Animals have hair overall its body')
            
        class mammals:
            def warmBlood(self):
                print('Mammals are warm blooded ')

        class bats(Animal,mammals):
            def print(self):
                print('bats are Mammals and Animals')

        b = bats()
        b.Hair()
        b.warmBlood()
    
    -> the object of bats class derived from both animal and mammals classes, and can use both functions from
        the two classes.

'''

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


# Question 2 (True or false):-
##############################

'''
1- Classes take memory space when they are created 
    -->(True)

2- Object Oriented Programming Provides logical structure to a program where programs are divided functions 
    -->(false)

3- Data Abstraction Allows showing important aspects while hiding implementation details 
    -->(True)

4- A constructor is a void method that has the same name as theclass and is used to initialize objects of 
that class. 
    -->(false)

5- Encapsulation is one of the 3 pillars of Object OrientedProgramming (OOP). It literally means to perceive 
an entity in a system or context from a particular perspective. We take out unnecessary details and only focus 
on aspects that are necessary to that context or system under consideration. 
    -->(True)

'''

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


# Question 3 ( Write Python Code ) :-
######################################

##### 1 #####
def count_vowels(w):
    vowels = 0
    word = w.lower()
    for i in word :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels +=1
    return vowels

print (f'The number of vowels in the word is {count_vowels("Celebration")}')
print('-----------------------------------------------------------------------------')

##### 2 ######
def sum_numbers(num):
    if num <1 :
        return 'Please enter a positive number !'
    elif num == 1:
        return num
    else:
        return num + sum_numbers(num-1)

print(sum_numbers(5))
print('-----------------------------------------------------------------------------')

##### 3 #####
num =10
def fibonacciSeries(num):
    if num <= 1:
        return num
    else:
        return (fibonacciSeries(num- 1) + fibonacciSeries(num - 2))

print("The Terms are :", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")
print('\n -----------------------------------------------------------------------------')

##### 4 #####
def checkInDict(dict,val):
    if val in dict.values():
        print(f'{val} present in a dict')
    else:
        print(f'{val} is not present in dict ')

sample_dict = {'a': 100, 'b': 200, 'c': 300}
checkInDict(sample_dict,200)
print('-----------------------------------------------------------------------------')

##### 5 #####
from cmath import pi

class Circle:
    def __init__(self , raduis , color):
        self.raduis = raduis
        self.color = color

    def getRaduis(self):
        return self.raduis

    def setRaduis(self , raduis):
        self.raduis = raduis

    def getColor(self):
        return self.color

    def setColor(self , color):
        self.color = color
    
    def getArea(self):
        return pow(self.raduis , 2) * pi

    def __str__(self):
        return f"Raduis = {self.raduis} \n color = {self.color} \n Area = {self.getArea()} \n Circumfernce = {self.getCircumference()}"

class Cylinder(Circle):
    def __init__(self,radius,color,height) :
        super().__init__(radius,color)
        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self,height):
        self.height = height
    
    def getVolume(self):
        return (pi*pow(self.raduis,2)*self.height)



########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

# Question 4 ( Make this possible ) :-
######################################

##### 1 #####
import string
import random

upperCaseLetters = list(string.ascii_uppercase)
lowerCaseLetters = list(string.ascii_lowercase)
digits = list(string.digits)

def generateRandomPassword():
    while True:
        try:
            passwordLength = int(input("Enter password lenght:"))
        except:
            print("please enter digits only")
            continue
        if passwordLength <8 :
            print("please enter at least 8 digits:")
            continue
        break

    password = []
    random.shuffle(upperCaseLetters) 
    random.shuffle(lowerCaseLetters)  
    random.shuffle(digits)

    for i in range(round(passwordLength * 0.4)):
        password.append(upperCaseLetters[i])
    for i in range(round(passwordLength * 0.3)):
        password.append(lowerCaseLetters[i])
    for i in range(round(passwordLength * 0.3)):
        password.append(digits[i])

    password = "".join(password[0:])
    print(f"The Generated password is --> \t {password}")

generateRandomPassword()
print('-----------------------------------------------------------------------------')


##### 2 #####
#Answered in separate File
#File Name :- Question 4-2


########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

# Question 5 ( Explain only by example  ) :-
##############################################

##### 1 #####

#Default constructor#
class person:
    def __init__(self): # no arguments
        self.name = 'mohameds'

#parameterized constructor#
class person:
    def __init__(self,id,name): # takes arguments
        self.id = id
        self.name = name


##### 2 #####

#Class# 
class Circle: # grouped data and properties
    def __init__(self , raduis , color):
        self.raduis = raduis
        self.color = color

    def getRaduis(self):
        return self.raduis

    def setRaduis(self , raduis):
        self.raduis = raduis

    def getColor(self):
        return self.color

    def setColor(self , color):
        self.color = color
    
    def getArea(self):
        return pow(self.raduis , 2) * pi

    def __str__(self):
        return f"Raduis = {self.raduis} \n color = {self.color} \n Area = {self.getArea()} \n Circumfernce = {self.getCircumference()}"

#Object#
c1 = Circle(4 , 'Red') # instance of the class is an object
c2 = Circle(3 , 'Blue')
