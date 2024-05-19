from collections import defaultdict
  
# initializing list
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Join Tuples if similar initial element
# Using defaultdict() + loop
mapp = defaultdict(list)
for key, val in test_list:
    mapp[key].append(val)
res = [(key, *val) for key, val in mapp.items()]
  
# printing result 
print("The extracted elements : " + str(res))