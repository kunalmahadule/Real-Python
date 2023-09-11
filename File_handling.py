'''
f = open('demo.txt','r')
f = open('demo.txt','w')
f.write("Jai Shree Krishna Jai Shree Krishna Jai Shree Krishna")
f = open('demo.txt')# by default read mode
p = f.read()
print(p)
p = f.readline() # read first line from the file
print(p)
p = f.read(5) # read first 5 character from the file
print(p)
f.close() 

# With statement-->f.close() do not need to write it automatically close

with open("demo.txt",'r') as f:
    a = f.read()
with open("demo.txt",'w') as f:
    a = f.write("monk")
print(a)


# Write a program to read the text from the file "poems.txt" and find out the file contain twinkle or not.
f = open('poem.txt', 'r')
p = f.read()
if "twinkle" in p:
    print("twinkle is present")
else:
    print("twinkle is not present")
'''   
# the game function in a program lets a user play a game and return a score as an intger. you need to read the any text file which is either blank or contains the privious high score you need to write the program to update the high score when game breaks the high score
'''
def game():
    return 211

score = game()
    
with open("hiscore.txt",'r') as f:
    hiscore = f.read()

if hiscore=='':
    with open("hiscore.txt",'w') as f:
        f.write(str(score))
elif score>int(hiscore):
    with open("hiscore.txt",'w') as f:
        f.write(str(score))

for i in range(2,21):
    with open(f"Tables/Multiplication_Table_of_{i}.txt","w") as f:
        for j in range(1, 11):
            f.write(f"{i}X{j} = {i*j}")
            if j != 10:
                f.write("\n")

# Write a program to print multiplication table from 1 to 20 in different files
for i in range(1,21):
    with open(f"tables/Multiplication_Table_of_{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j} = {i*j}")
            if j != 10:
                f.write("\n")

# Replace word donkey by ######## if any file contain donkey word
with open("poem.txt") as f:
    content = f.read()

if "donkey" in content:
    content = content.replace("donkey", "########")
    with open("poem.txt","w") as f:
        f.write(content)

# Replace some harmful words in list by ######## in the file

list = ["mote","sale","donkey","little"]

with open("poem.txt") as f:
    content = f.read()

for word in list:
    content = content.replace(word , "########")
    with open("poem.txt","w") as f:
        f.write(content)

# detect software word in a file or not

with open("demo.txt") as f:
    data = f.read()

if "software" in data.lower():
    print("software is present in file")
else:
    print("software is present in file")


# detect software word lineno. in file
data = True
i=1
with open("demo.txt") as f:
    while data:
        data = f.readline()
        if "software" in data.lower():
            print
            print(f"software is present in line no {i}")
        i=i+1

# make a copy of text file 
with open("this.txt") as f:
    info = f.read()  
with open("copy.txt","w") as f:
    f.write(info)

# check two txt file identical or not
with open("this.txt") as f:
    info1 = f.read()  
with open("copy.txt") as f:
    info2  = f.read()

if info1==info2:
    print("files are identical")
else:
    print("files are not identical")

# write a program to wipe out the content of the file
with open("demo.txt", "w") as f:
    f.write('')

# write a program to rename a file by rename_pyt.txt
import os
with open('this.txt') as f:
    info = f.read()
with open("rename_pyt.txt","w") as f:
    f.write(info)
    
os.remove("this.txt")
'''













