'''
getter 
setter
operator overloading
Function and Recursion
virtual environment
enumerate
List Comprehension

'''

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.


def firstElement(arr, n, k):
     
    # dictionary to count
    # occurrences of
    # each element
    for i in arr:
      count=0
      for j in arr:
        if i==j:
          count=count+1
      if count == k:
        return i
             
    # no element occurs k times
    return -1
 
# Driver Code
if __name__=="__main__":
 
    arr = [1,3,7, 4, 3,7, 4, 8];
    n = len(arr)
    k = 2
    print(firstElement(arr, n, k))
 
