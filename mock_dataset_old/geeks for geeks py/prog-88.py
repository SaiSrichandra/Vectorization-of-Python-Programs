test_str = 'geeksforgeeks'
  
# printing original string
print("The original string is : " + str(test_str))
  
# initializing substring
K = 'seek'
  
# concatenating required characters 
temp = lambda sub: ''.join(chr for chr in sub if chr in set(K))
  
# checking in order
res = K in temp(test_str)
  
# printing result 
print("Is substring in order : " + str(res))