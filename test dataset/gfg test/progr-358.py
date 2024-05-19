import re  
  
# url link
s = 'file://localhost:4040/abc_file'
  
# finding the file capture group
obj1 = re.findall('(\w+)://', s)  
print(obj1)
  
# finding the hostname which may 
# contain dash or dots
obj2 = re.findall('://([\w\-\.]+)', s)
print(obj2)
  
# finding the hostname which may 
# contain dash or dots or port
# number
obj3 = re.findall('://([\w\-\.]+)(:(\d+))?', s)
print(obj3)