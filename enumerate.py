list1 = [10,20,"Harry",44.3,False]

# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

# The enumerate function adds counter to an iteratable and return it
for index, item in enumerate(list1):
    print(item, index)
             # |->This return index of items
             
             
for item in enumerate(list1):
    print(item)
 

