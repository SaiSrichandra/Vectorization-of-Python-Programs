import re
 
# initialising string
ini_string = "123abcjw:, .@! eiw"
 
# printing initial string
print ("initial string : ", ini_string)
 
# function to demonstrate removal of characters
# which are not numbers and alphabets using re
getVals = list([val for val in ini_string
               if val.isalpha() or val.isnumeric()])
 
result = "".join(getVals)
 
# printing final string
print ("final string", result)