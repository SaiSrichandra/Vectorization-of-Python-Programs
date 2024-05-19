test_list = ["geeks", "for", "geeks", "is", "best"]
  
# printing original list
print ("The original list is : " + str(test_list))
  
# Reverse All Strings in String List
# using map()
reverse = lambda i : i[::-1]
res = list(map(reverse, test_list))
  
# printing result
print ("The reversed string list is : " + str(res))