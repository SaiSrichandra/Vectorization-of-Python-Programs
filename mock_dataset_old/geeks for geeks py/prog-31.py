import re
 
sampleInput = "1001010"
 

c = re.compile('[^01]')
if(len(c.findall(sampleInput))):
    print("No") # if length of list > 0 then it is not binary
else:
    print("Yes")