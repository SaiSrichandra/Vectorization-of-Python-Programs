def Cloning(li1):
    li_copy = li1[:]
    return li_copy
li1 = []   
# Driver Code
n = input("Enter len")
for i in range(n):
     li1.append(input("Enter no"))
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)