import re
  
# initializing string
test_str = "geeks4feeks is No. 1 4 geeks"
  
# printing original string
print("The original string is : " + test_str)
  
# Frequency of numbers in String
# Using re.findall() + sum()
res = sum(1 for _ in re.finditer(r'\d+', test_str)) 
  
# printing result 
print("Count of numerics in string : " + str(res))