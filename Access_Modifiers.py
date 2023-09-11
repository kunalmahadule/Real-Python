# Public Access Modifier:
# The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default. 

# program to illustrate public access modifier in a class

class Geek:
	
	# constructor
	def __init__(self, name, age):
		
		# public data members
		self.geekName = name
		self.geekAge = age

	# public member function	
	def displayAge(self):
		
		# accessing public data member
		print("Age: ", self.geekAge)

# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()


# output:
# Name:  R2J
# Age:  20
 

# In the above program, geekName and geekAge are public data members and displayAge() method is a public member function of the class Geek. These data members of the class Geek can be accessed from anywhere in the program.

