import random

def rand_key(p):
   
    # Variable to store the
    # string
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(p):

        temp = str(random.randint(0, 1))
 

        key1 += temp
         
    return(key1)
 
# Driver Code
n = 7
str1 = rand_key(n)
print("Desired length random binary string is: ", str1)