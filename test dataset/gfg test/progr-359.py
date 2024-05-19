import re
  
# url
s = 'http://www.example.com/index.html' 
  
# searching for all capture groups
obj = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)',
                 s)
  
print(obj)