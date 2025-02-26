test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Join Tuples if similar initial element
# Using loop
res = []
for sub in test_list:                                           
    if res and res[-1][0] == sub[0]:              
        res[-1].extend(sub[1:])                        
    else:
        res.append([ele for ele in sub])     
res = list(map(tuple, res))
  
# printing result 
print("The extracted elements : " + str(res))