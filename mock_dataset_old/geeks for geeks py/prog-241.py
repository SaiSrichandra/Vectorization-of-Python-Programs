import re
 
# initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Extract digits from Tuple list
# Using regex expression
temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
res = [int(ele) for ele in set(temp)]
 
# printing result
print("The extracted digits : " + str(res))