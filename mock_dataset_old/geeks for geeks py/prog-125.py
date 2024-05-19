list1 = [10, 21, 4, 45, 66, 93, 11]
  
even_count, odd_count = 0, 0
num = 0
  
# using while loop     
while(num < len(list1)):
      
    # checking condition
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
      
    # increment num 
    num += 1
      
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)