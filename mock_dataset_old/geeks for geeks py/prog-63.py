test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
  
# printing original list 
print("The original list : " + str(test_list))
  
# initialize suffix
suff = 'x'
  
# Suffix removal from String list
# using loop + remove() + endswith()
for word in test_list[:]:
    if word.endswith(suff):
        test_list.remove(word)
  
# printing result
print("List after removal of suffix elements : " + str(test_list))