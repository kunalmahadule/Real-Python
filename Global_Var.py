a = 44 # Global Variable
def display():
    global a # Changing the value of a by 9
    print(a)
    a = 9 # Local Variable
    print(a)

display()
print(a)
 
