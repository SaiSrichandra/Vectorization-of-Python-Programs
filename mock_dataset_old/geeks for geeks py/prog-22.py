from collections import Counter
from itertools import chain
  
# initializing lists
test_list = ["geeksforgeeks is best for geeks"]
  
# printing original list
print("The original list : " + str(test_list))
  
# char list 
chr_list = ['e', 'b', 'g']
  
# dict comprehension to retrieve on certain Frequencies
# from_iterable to flatten / join
res = {key:val for key, val in dict(Counter(chain.from_iterable(test_list))).items() if key in chr_list}
      
# printing result 
print("Specific Characters Frequencies : " + str(res))