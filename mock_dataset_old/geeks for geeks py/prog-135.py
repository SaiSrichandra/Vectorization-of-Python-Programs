def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
  
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print (Remove(tuples))