test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing Custom eles
cus_eles = [6, 7, 8]
  
# Row-wise element Addition in Tuple Matrix
# Using zip() + list comprehension
res = [[(idx, val) for idx in key] for key,  val in zip(test_list, cus_eles)]
  
# printing result 
print("The matrix after row elements addition : " + str(res))