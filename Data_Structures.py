# List
'''
a = [1,2,4,55,6]
print(a[0])
print(a[1])
a[3] = 45
print(a[3])

list = [12, "mango", False, 222.32]
print(list) 

# list slicing

list1 =["harry", "rohan", "mayur", "raj", "tom", "sam"]
print(list1[0:4])
print(list1[-6:-2]) # negative indixing


# list methods
sort
insert
append
reverse
pop
remove

lst = [10,2,43,53,5,3,55]
print(lst)
# lst.sort()
# lst.append(66)
# lst.reverse()
# lst.pop(3)
# lst.remove(55)
# lst.insert(2, 90)
print(lst)
'''



# Tuple-->do not change the value of tuple
'''
tuple1 = () # empty tuple
tuple2 = (1,) # tuple with single item
tuple3 = (10,20,30)

print(tuple1)
print(tuple2)
print(tuple3)

# tuple methods

index 
count

tuple4 = (2,4,3,2,54,34,2)
print(tuple4.count(2)) # count 2 how many time in tuple
print(tuple4.index(3)) # return index no. of 3


M1 = int(input("Enter the marks1 "))
M2 = int(input("Enter the marks2 "))
M3 = int(input("Enter the marks3 "))
M4 = int(input("Enter the marks4 ")) 
M5 = int(input("Enter the marks5 "))
M6 = int(input("Enter the marks6 "))

ls = [M1,M2,M3,M4,M5,M6]
ls.sort()
print(ls)

# program to sum a list
listt = [10,20,30,40]
print(listt[0]+ listt[1]+listt[2]+ listt[3])


# program to count no. of zeros
a = (7,0,8,0,0,9,0)
print(a.count(0))
'''



# Dictionary

'''
mydict = {
    "value1" : "harry",
    "value2": "Neon",
    "value3":[10,20,30],
    "value4":{1:"one",
              2:"two",
              3:{5:"hanuman",
                 6:"Ram"}
            }
}

# print(mydict["value4"][2])
# print(mydict["value3"])

# Dictionary Methods 

keys()
values()
items()
update()
get()


# print(type(mydict))
# print(type(mydict.keys()))
# print(list(mydict.keys()))
# print(mydict["value4"][3][6])
# print(mydict.values())
# print(mydict.items())
print(mydict)
li = {"value8":[11,12,13],
      "value1":"kunal"} # 
mydict.update(li)
print(mydict)

print(mydict.get("value8")) # if key is not present return None
print(mydict["value8"]) # if key is not present return error
'''



# Sets
''''''
# a = {1,2,3,4,1}
# print(a) # repeated value is ignored by set
# print(type(a))

# b = {} #This will create empty Dictionary not empty set
# c = set() #for creating empty set
# print(type(c))

# Set Methods
'''
add()
len()
remove()only remove the element
pop()remove element as well as return it
clear()empty the set
union()
intersection()


c.add(10)
c.add(11)
c.add(12)
c.add(10)
# c.add([10,20,30])
# c.add({2:4})-->This is unhashable type
c.add((10,20,30))#This is hashable type
# Important: you enter tuple in the set but list , dict not enter in set because list , dict change their values
print(c)
print(len(c))
c.clear()
print(c)
# print(c.remove(12))
# print(c.pop())
'''

'''
# Practice Set

# 1. Write a program to create a dictionary of hindi words

dict11 ={
      "Pankha":"Fan",
      "palang":"Bed",
      "basta":"Bag"
}

print(dict11.keys())
print("Enter a hindi word to want conversion in English")
a = input("Enter the hindi word ")
print("Your Hindi word is", dict11.get(a))


# 2.Write a program to input eight numbers from a user and display all unique number at once

I1 = int(input("Enter no. 1 "))
I2 = int(input("Enter no. 2 "))
I3 = int(input("Enter no. 3 "))
I4 = int(input("Enter no. 4 "))
I5 = int(input("Enter no. 5 "))
I6 = int(input("Enter no. 6 "))
I7 = int(input("Enter no. 7 "))
I8 = int(input("Enter no. 8 "))

set1 = {I1,I2,I3,I4,I5,I6,I7,I8}
print(set1)


# 3.
Set = {20,20.0,"20"}
print(Set)
print(len(Set))#it gives length=2 because 20 and 20.0 value same hone ki vajha se dono values ko 1 element man raha hai

# 4,What is the type of S.  where s = {}
s ={}
print(type(s))


# 5.

favLang = {}

a = input("Enter your favourite language Subham \n")
b = input("Enter your favourite language ankit \n")
c = input("Enter your favourite language rohan \n")
d = input("Enter your favourite language mayur \n")

favLang["Subham"] = a
favLang["ankit"] = b
favLang["rohan"] = c 
favLang["mayur"] = d

print(favLang)
'''

# print("kunal "* 10)
