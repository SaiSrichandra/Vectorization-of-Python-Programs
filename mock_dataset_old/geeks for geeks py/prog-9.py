def word_both_cap(str):
      
    
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), 
                        s.title().split()))
      
      
# Driver's code
s = "welcome to geeksforgeeks"
print("String before:", s)
print("String after:", word_both_cap(str))