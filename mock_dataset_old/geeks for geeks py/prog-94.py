test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
  
# printing original lists
print("The original list is : " + str(test_list))
  
# Swap elements in String list
# using replace() + join() + split()
res = ", ".join(test_list)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')
  
# printing result 
print ("List after performing character swaps : " + str(res))