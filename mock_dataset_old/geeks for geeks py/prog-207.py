test_tup = (1, 5, 7, 8, 10)
  
# printing original tuple
print("The original tuple : " + str(test_tup))
  
# Adjacent element multiplication
# using tuple() + map() + lambda
res = tuple(map(lambda i, j : i * j, test_tup[1:], test_tup[:-1]))
  
# printing result
print("Resultant tuple after multiplication : " + str(res))