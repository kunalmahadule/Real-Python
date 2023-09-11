# Object Oriented Programing in Python

'''
class
object
class attribute
object attribute
Self parameter
'''
'''
# Creating class
class Employee:
    # class attribute
    company = "Google"
    salary = 10000
    # class method
    def display_Com(self): # self parameter automatically call when object call the method
        print("This is my first class")

# Creating Object
harry = Employee()
# Object attribute
harry.name = "Harry's Khan"
print(harry.salary)
harry.salary = 5000000  # updating class attribute
print(harry.salary)
print(harry.company)
print(harry.name)
harry.display_Com()#method takes object as a parameter by default see below line
# Employee.display_Com(harry) #This line help to understand self parameter

# Static method
# If you want to run your method without self use static method
class Student:
    Id = 101
    name = "Harry"
    
    def printInfo(self,Id,name):
        print(f"The name of the student is {self.name} and id is {self.Id}")
    
    @staticmethod
    def Greet():   # This method only print statement don't need any parameter
        print("Congrulations, for your achievement!")

Rajni = Student()
Rajni.printInfo(Rajni.Id,Rajni.name)
Rajni.Greet()

# Constructor
# Type 1
class Programer: 
    def __init__(self,name,language):
        print("Object is Created!")
        print(f"The name of the Programer is {name} and language is {language}")
        
harry = Programer("Harry","Python")
# Type 2
class Programer: 
    def __init__(self,name,language):
        self.name = name
        self.language = language
        print("Object is Created!")
        self.print_detail()
    
    def print_detail(self):
        print(f"The name of the Programer is {self.name} and language is {self.language}")
        
harry = Programer("Harry","Python")
'''
'''
# PRACTICE SET

# 1 Create a class Programer and store some info about programers working for microsoft
class Programer:
    company = "Microsoft" 
    
    def __init__(self,name,Product):
        self.name = name
        self.Product = Product
        print("Object is Created!")
        self.print_detail()
    
    def print_detail(self):
        print(f"The name of the {self.company} Programer is {self.name} and Procuct is {self.Product}")
        
harry = Programer("Harry","Windows")
alka = Programer("alka","GitHub")

# 2 Write a class Calculator capable of finding square, squareroot & cube of no.
class calculator:
    def __init__(self,num):
        self.number = num
        self.square()
        self.squareroot()
        self.cube()
        
    def square(self):
        print(f"The square of given {self.number} is {self.number **2}")
    
    def squareroot(self):
        print(f"The square of given {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The square of given {self.number} is {self.number **3}")

Number = calculator(9)

# 3 by changing object attribute leads to change class attribut yes & no?
class Calculator:
    add = "addition"

c = Calculator()
c.add = "plus"
print(c.add)
print(Calculator.add) #before changing
Calculator.add = "milaoo" # That leads to change class attribute
print(Calculator.add) #after changing

# 4 add static method in problem 2
class calculator:
    def __init__(self,num):
        self.number = num
        self.square()
        self.squareroot()
        self.cube()
                
    def square(self):
        print(f"The square of given {self.number} is {self.number **2}")
    
    def squareroot(self):
        print(f"The square of given {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The square of given {self.number} is {self.number **3}")
    
    @staticmethod
    def greet():
        print("This is the best calculator in the world")

Number = calculator(9)
Number.greet()

# 5 Write a class train which has method to book a ticket, getstatus(no of seats) and get fare info of trains running under indian railways.
class Train:
    name = "Channei Express"
    no_Of_Seats = 2
    Price = 70
    
    def get_status(self, no_Of_Seats):
        print(f"The train {self.name} available seats is {self.no_Of_Seats}")
        
    def get_fair(self, Price):
        print(f"The price of train ticket is {self.Price} Rs")
        
    def book_Ticket(self):
        if self.no_Of_Seats>0:
            print(f"Your ticket is successfully book and seat no is {self.no_Of_Seats}")
            self.no_Of_Seats = self.no_Of_Seats - 1 
        else:
            print("Sorry, Ticket is not available try tatkal")

    # If a customer cancel the ticket add seat increment by 1
    def ticket_Cancel(self):
        self.no_Of_Seats = self.no_Of_Seats + 1
    
P1 = Train()
P1.get_status(P1.no_Of_Seats)
P1.get_fair(P1.Price)
P1.book_Ticket()
P1.book_Ticket()
P1.ticket_Cancel()
P1.book_Ticket()

# 6 Can you change a self parameter inside a method to something else (slf). Try changing self to slf and see the effects
class Train:
    name = "Channei Express"
    no_Of_Seats = 2
    Price = 70
    # Successfully change the name of parameter self by slf and hence there is no effect
    def get_status(slf, no_Of_Seats):
        print(f"The train {slf.name} available seats is {slf.no_Of_Seats}")
        
P1 = Train()
P1.get_status(P1.no_Of_Seats)
'''
'''
# Inheritance
single
multiple 
multilevel

# Program of Inheritance or single Inheritance
class A:
    a = 10
    animal = "Lion"

class B(A):
    a = 111
b = B()
print(b.a,"\n",b.animal)

# Multiple Inheritance
class Father:
    salary = 20000
    def gift(self):
        print("Video game")
    
class Mother:
    salary = 30000
    def dish(self):
        print("Ice-Cream")
    
class child(Mother,Father):
    pass

ch1 = child()
print(ch1.salary)
ch1.dish()
ch1.gift()

# Multilevel Inheritance
class A:
    a =10
    joke = "Hello world"

class B(A):
    b = 1010
    joke = "Hello"
    
class C(B):
    pass

c1 = C()
print(c1.a)
print(c1.b)
print(c1.joke)

# Super() method
# example 1
class A:
    a =10
    joke = "Hello world"

class B(A):
    b = 1010
    joke = "Hello"
    def dis(self):
        print("oppo")
        
class C(B):
    joke = "oppo"
    def dis(self):
        super().dis()
        print("vivo")
        
c1 = C()
c1.dis()

# example 2
class Father:
    salary = 20000
    def __init__(self):
        print("Father class")
        
    def gift(self):
        print("Video game")
    
class Mother:
    salary = 30000
    def __init__(self):
        print("Mother class")
    
    def dish(self):
        print("Ice-Cream")
    
class child(Mother,Father):
    def gift(self):
        # super().__init__()
        super().gift()
        print("GTA")

cc = child()
cc.gift()

# Class method
class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # # One way to modify class attributes
    # def changeSalary(self, sal):
    #     self.__class__.salary = sal
    
    @classmethod    # Way to access class attributes
    def changeSalary(cls, sal):
            cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(344)
print(e.salary)
print(Employee.salary)

# property decorator/getter
10:30:00-------->timestamp
class Employee:
    company ="TCS"
    salary = 1000
    salaryBonus = 500
    # totalSalary = 1200
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter     #setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary
        
e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salaryBonus)

# Operator Overloading
# 10:45:00---------->timestamp
# two number object ko add karne ke liye __add__
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):   #sum karna hai to __add__ python doc me given hai
        print("Let's add")
        return self.num + num2.num
    
    def __mul__(self, num2):   #mul karna hai to __mul__ python doc me given hai
        print("Let's multiply")
        return self.num * num2.num
    
n1 = Number(4)  # integer Object
n2 = Number(6)
sum = n1+n2
print(sum)

mul = n1*n2
print(mul)

# Other dunder mehtods
# 10:50:00--------->timestamp







# Problem set
# 1 Create a class C_2D_vector and use it to create another class represent a C_3D_vector
class C_2D_vector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
class C_3D_vector(C_2D_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2 = C_2D_vector(3, 7)
v3 = C_3D_vector(2, 9, 5)
print(v2)
print(v3)

# 2 Create a class pet from animal class further create class dog form pet class and create bark method in dog
class Animal:
    Category = "A"
    Breed = "Jerman"
    def printDetails(self):
        print(f"The Category of the Animal is {Animal.Category} and Breed is {Animal.Breed}")
        
class Pet(Animal):
    pass

class Dog(Pet):
    @staticmethod
    def bark():
        print("Bow Bow...............!")

d = Dog()
d.bark()

# 3 Create a class Employee and add salary and increment prop. to it write a mehtod salaryAfterIncrement method with a @property decorator with a setter with changes the value of increment based on the salary.
# 11:05:00-------------->timestamp
class Employee:
    salary = 10000
    incrementProperty = 1.2
    
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.incrementProperty

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.incrementProperty = sal/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.incrementProperty)
e.salaryAfterIncrement = 15000
print(e.incrementProperty)

# 4 Write a class complex to represent complex numbers along with overloaded operators + and * which adds and multiply them

# (a+bi)(c+di) = (ac-bd) + (ad+bc)
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
        
    def __add__(self, c):
        return Complex(self.real+c.real, self.imaginary+c.imaginary)
    
    def __mul__(self,c):
        mulReal = self.real*c.real-self.imaginary*c.imaginary
        mulImgi = self.real*c.imaginary+self.imaginary*c.real
        return Complex(mulReal,mulImgi)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)
print(c1*c2)

# 5 Write a class vector represent a vector on n dimension. Overload the + and * operator which calculates the sum and the dot product of them.

class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
        
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
        
v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

print(v1+v2)
print(v1*v2)

# 6 Write __str__() method to print the vector as follows 7Î + 8ĵ + 10k^ suppose vector of dimension 3 for this problem
class Vector:  
    def __init__(self, vec):
        self.vec = vec
        
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])

print(v1)
print(v2)

# 7 Override the __len__() mehtod on vector of problem 5 to display the dimension of the vector 

class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
        
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)
        
v1 = Vector([1, 4, 6, 5, 2])
v2 = Vector([1, 6, 9])

print(len(v1))
print(len(v2))
'''

# Assignment--> if the vector length not same during the time of addition or multiplication so return error message (in problem 7)

class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
        
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)
        
v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9, 8, 6])
l1 = len(v1)
l2 = len(v2)

if l1 == l2:
    print("The addition and multiplication of two vectors is")
    print(v1+v2)
    print(v2*v2)
    print("\n")
    print("The length of two vectors is")
    print(len(v1))
    print(len(v2))
    
else:
    print("The length of two vectors are not same")















'''
# CHATGPT TESTING
# add two numbers code in python

# Inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum = num1 + num2

# Output
print("The sum of", num1, "and", num2, "is", sum)
'''
