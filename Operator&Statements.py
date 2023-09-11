'''
# is and in operator
a = 88
if a is 88:
    print("Yes")
else:
    print("No")

listt = [10,20,30,40]
print(20 in listt)# return true
print(200 in listt)# return false

# logical operator
age = 11
if age>1 and age<100:
    print('Yes')
elif age==11:
    print("Yo Yo")
else:
    print("No")



# 1.Write a program to find greatest of four numbers entered by user
# Done through my logic
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))


list2 = [num1,num2,num3,num4]
# lisa = list.sort()
# print(list2)
list2.sort()
# print(list2)
print("The gretest number is", list2[3])

# harry logic

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1>num4:
    f1 = num1
else:
    f1 = num4   

if num2>num3:
    f2 = num2
else:
    f2 = num3

if f1>f2:
    print(f1, "is the greater number")
else:
    print(f2, "is the greater number")


# Write a program to find out wheather the student pass or fail, it require 40% and at least 33% in each subject and take marks as a input from the user.

sub1 = int(input("Enter subject 1 marks : "))
sub2 = int(input("Enter subject 2 marks : "))
sub3 = int(input("Enter subject 3 marks : "))

total = sub1+sub2+sub3;

if sub1<33 or sub2<33 or sub3<33:
    print("You fail in one subject")    
elif total/3<44:
    print("You Fail")
else:
    print("You Passed")

# A spam comment is defined as a text containing following keywords "make a lot of money" "buy now" "suscribe now" "click this". Write a program to detect this spam

message = input("Enter a Message ")

if "make a lot of money" in message:
    spam = True
elif "buy now" in message:
    spam = True
elif "suscribe now" in message:
    spam = True
elif "click this" in message:
    spam = True
else:
    spam = False
    
if(spam):
    print("This message is Spam")
else:
    print("This message not is Spam")

# Write a program find wheather the given username contain less than 10 character or not.

username = input("Enter username : ")
if len(username)<10:
    print("Username do not contain 10 char ")
else:
    print("Username contain 10 char ")

# Write a program to calculate a grade of a student from his marks 
# 90-100 - ex
# 80-90 - a
# 70-80 - b
# 50-70 - c
# <50 - d

marks = int(input("Enter your marks : "))

if marks>=90:
    print("Excellent")
elif marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
else:
    print("You Fail")
'''

# write a program to find out wheather a given post talking about harry or not

post = input("Enter your post : \n")

if "harry" in post:
    print("Yes")
else:
    print("No")
    