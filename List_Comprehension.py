'''
# List Comprehension is an elegant way to create list based on exitsting list
a = [10,2050,555,404,4,2,5,6,6,3,3,56]
b=[]

# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)

# # set Comprehension
# t = [10,203,330,33]
# set1 = {i for i in t if i%2==0}
# print(set1)
'''




'''
Practice set--->Topic 
Exception handling
creating a module
global variable
enumerate
list comprehension


# 1 Write a program to open the three files 1.txt, 2.txt & 3.txt if any file is not present than show error message

def readFiles(fileName):
    try:
        with open(fileName, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"{fileName} file not found")
        
readFiles("1.txt")
readFiles("2.txt")
readFiles("3.txt")

# 2 Write a program to print third, fifth and seventh element from a list using enumerate function

list0 = [1,2,3,4,5,6,7,8,9,10]

for index, item in enumerate(list0):
    if index==2 or index==4 or index==6:
        print(item, end=" ")

# 3 Write a list Comprehension to print a list which contains the multiplication table of a user entered numbered.
# b = [i for i in a if i%2==0]

try:
    num = int(input("Enter the number you want multiplication table: "))
    # using List comprehnsion
    table=[num*i for i in range(1,11)]
    print(table)
    
    # for i in range(1, 11):
    #     print(f"{num} X {i} = {num*i}")
except ValueError:
    print("Please enter a valid value")

# 4 Write a program to display a/b a and b are integers. If b=0 display infinite by handling the ZeroDivisionError

try:
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print(a/b)
    
except:
    print("Infinity")


# 5 Store the multiplication table generate in problem 3 in the file named Tables.txt
try:
    num = int(input("Enter the number you want multiplication table: "))
    # using List comprehnsion
    table=[num*i for i in range(1,11)]
    print(table)
    
    with open("Tables.txt", "a") as f:
        f.write(str(table))
        f.write("\n")

except ValueError:
    print("Please enter a valid value")
'''

# --->Timestamp - chapter 13 virtual Environment--1:15:00







