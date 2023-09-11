def square(num):
    return num*num
# Method 1
a = [1, 2, 3]
l = []
for item in a:
    l.append(square(item))

# print(l)

# Method 2
print(list(map(square, a))) # map ne a ke sare element ke liye square ko chalaya


