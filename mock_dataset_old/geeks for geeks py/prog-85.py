import re
  
# initializing strings
test_str = 'geeksforgeeks is best 4 geeks'
  
# printing original string
print("The original string is : " + str(test_str))
  
# slicing after the numeric occurrence
res = re.match(r"(.*\d+)", test_str).group()
  
# printing result 
print("The string after removal : " + str(res))