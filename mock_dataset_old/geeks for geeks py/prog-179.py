
# Initializing list
test_list = ['Gfg is best', 'for Geeks', 'Preparing']

# printing original list
print("The original list is : " + str(test_list))

K = ' '

# Split String of list on K character
# using join() + split()
res = K.join(test_list).split(K)

# printing result
print ("The extended list after split strings : " + str(res))