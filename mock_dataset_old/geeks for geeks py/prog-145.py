from itertools import chain
import random
  
# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# choice() for random number, from_iterables for flattening
res = random.choice(list(chain.from_iterable(test_list)))
  
# printing result
print("Random number from Matrix : " + str(res))