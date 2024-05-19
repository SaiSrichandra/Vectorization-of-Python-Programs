import random
  
# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing Row number
r_no = 1
  
# choice() for random number, from_iterables for flattening
res = random.choice(test_list[r_no])
  
# printing result
print("Random number from Matrix Row : " + str(res))