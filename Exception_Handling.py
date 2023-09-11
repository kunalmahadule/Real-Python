
'''
# Exception handling
try:
    num = int(input("Enter the number "))
    print(num + 1)
except:
    print("Enter only numerical value")


# Handling different Exceptions
try:
    a = int(input("Enter a number: "))
    c = 13/a
    print(c)

except ValueError as e:
    print("Make sure you not enter any string")

except ZeroDivisionError as e:
    print("Make sure you are not divide by 0")

# If any other exception has occured than execute this block   
except Exception as e:
    print(e)


# Raising Exceptions
# we can raise custom exception using raise keyword
def Incrementer(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Enter only Integer value")
        

# a = Incrementer('3kjn3') # This line throw ValueError
a = Incrementer("36")
print(a)



# try with else clause
try:
    i = int(input("Enter a number: "))
    c = 22/i
except:
    raise ValueError("Enter only number")
# If try block is successfully executed than else block executed
else:
    print("Program is successfully executed!")

'''
# try with finally clause
try:
    i = int(input("Enter a number: "))
    c = 22/i
except Exception as e:
    print(e)
    exit() # exit the program 
# This block is always executed even program is exit()
finally:
    print("Program is successfully executed!")

print("It is done")
