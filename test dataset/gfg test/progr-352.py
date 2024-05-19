ini_string = "123abcjw:, .@! eiw"
 
# printing initial string
print ("initial string : ", ini_string)
 
k = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
# function to demonstrate removal of characters
# which are not numbers and alphabets using filter and in
getVals = list(filter(lambda x: x in k,  ini_string))
result = "".join(getVals)
 
# printing final string
print ("final string", result)