'''
i = 0
while i<10:
    print("Yes " + str(i))
    i = i+1


# for loop with else
# print multiplication table from while loop
num = int(input("Enter the number for multiplication table : "))
i = 1
while i<=10:
    print(i*num)
    i = i + 1

# print list element  using loop
l = [10,100,1000,10000,100000]
i=0
for i in range(0,len(l)):
    print(l[i])
    i = i + 1

# fstring
print(f"{12} X {2} = {12*2}")

# Greet the member names start with S

l1 = ['Harry','Sohan','Sachin','Rahul']
for name in l1:
    if name.startswith('S'):
        print('Hello ' + name)

# Write a program to find wheather given number is prime or not

a = int(input("Enter a number : "))
prime = True

for i in range(2,a):
    if a%i == 0:
        prime = False
    
if prime:
    print("The number is prime")
else:
    print("The number is not prime")

# Write a program to find the sum of first n natural numbers using while loop
num = int(input("Enter the number : "))
sum = 0
i = 1
while i<=num:
    sum = sum + i
    i = i + 1
print(sum)

# Write a program to calculate factorial of a given number using for loop

num = int(input("Enter the number : "))
f = 1
for i in range(1,num+1):
    f = f * i
    i = i - 1
print(f"The factorial {num} is {f}")

# Write a program to print this pattern
# *
# **
# ***
# ****
for i in range(5):
    print("*"*i)


# Write a program to print this pattern
#   *
#  ***
# *****
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

# Write a program to print this pattern
# * * *  
# *   * 
# * * *
for i in range(3):
    if i==0:
        print("* " * 3)
    elif i == 1:
        print("*  "+" *")
    else:
        print("* "*3)
        break;
'''        

# Write a program to print multiplication table in reverse order using for loop

num = int(input('Enter a number '))
n = 10
for i in range(0,10):
    table = n * num
    n = n - 1
    print(table)





