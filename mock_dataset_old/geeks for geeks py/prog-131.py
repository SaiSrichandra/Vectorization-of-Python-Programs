list1 = [10, -21, -4, 45, 66, 93, -11]
  
neg_count = len(list(filter(lambda x: (x < 0), list1)))
  
# we can also do len(list1) - neg_count
pos_count = len(list(filter(lambda x: (x >= 0), list1)))
  
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)