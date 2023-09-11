def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False
    
li = [1,2,3,4,5,6,7,8,96,5,3,2,3,65]
print(list(filter(greater_than_5,li))) # li ke sare element ke liye filter ne greater_than_5 function chalaya