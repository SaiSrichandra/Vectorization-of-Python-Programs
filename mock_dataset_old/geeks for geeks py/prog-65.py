test_string = "geekforgeeks"
  
# printing original string 
print("The original string : " + str(test_string))
  
# using sorted() + reduce() + lambda
# Reverse Sort a String
res = reduce(lambda x, y: x + y, sorted(test_string, reverse = True))
      
# print result
print("String after reverse sorting : " + str(res))