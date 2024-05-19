test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
  
# printing original list
print("The original list : " + str(test_list))
  
# initializing key list 
key_list = ["name", "number"]
  
# using list comprehension to perform as shorthand
n = len(test_list)
res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx + 1]}
       for idx in range(0, n, 2)]
  
# printing result 
print("The constructed dictionary list : " + str(res))