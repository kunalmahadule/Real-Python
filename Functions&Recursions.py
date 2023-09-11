# Recursion ek aisa function jo khud ko call karta hai
"""
# function
def sum(a, b): 
    return a+b

add = sum(10, 10)
print(add)

# Recursion
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product

g = factorial_iter(1)
print(g)

def factorial_recursive(n):
    if n == 1 or n== 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)




# Write a program to find the greatest of three numbers using functions
def maximum(num1, num2, num3):
    if num1>num2:
        return num1
        if num1>num3:
            return num1
    
    if num2>num3:
        return num2
    else:
        return num3

a = int(input())
b = int(input())
c = int(input())
max = maximum(a,b,c)
print(max)

# Write a program to find the greatest of four numbers using functions
def max_number(a, b, c, d):
    if a > b:
        if a > c:
            if a > d:
                return a

    if b > a:
        if b > c:
            if b > d:
                return b

    if c > a:
        if c > b:
            if c > d:
                return c

    if d > a:
        if d > c:
            if d > b:
                return d

a = int(input())
b = int(input())
c = int(input())
d = int(input())
output = max_number(a, b, c, d)
print("The max number is ", output)


# Write a python program using function to convert celsius to fahrenhit
# 0 celcious = 32 ferehnite

def Convert_Celcius_to_Fahrenhit(a):
    c = (a*(9/5)) + 32
    return c

a = int(input("Enter Temperature in celcius and we convert that ino celcius\n"))
o = Convert_Celcius_to_Fahrenhit(a)
print(o)

# How do you prevent a python print() function to print a new line at the end.
print("Hello", end=" ")
print("Hello", end=" ")
print("Hello", end=" ")

# n! = (n-1)! * n
# sum(n) = sum(n-1) + n
sum = 0 
def natural_Sum(n):
    sum = sum(n-1) + n
    return sum
a = int(input("Enter the number "))
v = natural_Sum(a)
print(v)
This problem not solve completely


# print following patter
# * * *
# * *
# * 
n = 3
for i in range(0, n):
    print("*" * n)
    n -= 1
"""

# convert inches to cm

# Write a python program to remove a given word from the string and strip it at the same time


def remove_word(line, word):
    return line.replace(word, "")


line = "      premium notebook is good bad     "
word = "good"
res = remove_word(line, word)
print(res.strip())
