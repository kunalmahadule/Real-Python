# str = "Harry"
# str[0] = "  "-->does not work 
# print(str[-4])
# print(str[-5:])-->is same as str[0:]
# print(str[:])

# Functions of Strings
# story = "jai Hind"
# print(len(story))
# print(story.endswith('d'))
# print(story.count('i'))
# print(story.count('jai'))
# print(story.index('H'))
# print(story.capitalize())
# print(story.find("harry"))
# print(story.find("Hind"))
# print(story.replace("Hind", "Maharashtra"))
# print(story)

# 1.
# Greeting = input("Enter your name ")
# print("Good Afternoon", Greeting)

# 2.
# letter = '''Dear <|NAME|>
#         I am happy to invite you about your selection.
        
#         date: <|DATE|>
#             '''

# name = input("Enter your name\n")
# date = input("Enter date\n")
# letter = letter.replace("<|NAME|>",name)            
# letter = letter.replace("<|DATE|>",date)            
# print(letter)

# 3.Write a program to detect double spaces in the string
'''
Essay = "This is a  String with  double spaces"
print(Essay)
print(Essay.find("  "))
Essay = Essay.replace("  "," ")
print(Essay)
'''

# write a program to formate a following letter by using escape sepuences characters

letter = "Dear Harry,\n \tThis python course is nice.\n Thanks!"
print(letter)