from itertools import count
  
# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing K
K = 20
  
# count() for getting count
# pairing using zip()
cnt = count()
res = next(j for sub in test_list for j, idx in zip(
    range(len(sub)), cnt) if idx == K)
  
# printing result
print("Index of character at Kth position word : " + str(res))