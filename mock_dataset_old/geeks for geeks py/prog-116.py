def myMax(list1):
    max = list1[0]

    for x in list1:
        if x > max :
             max = x
      
    # after complete traversing the list 
    # return the "max" value
    return max
  
  
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))