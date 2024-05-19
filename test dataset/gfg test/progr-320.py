import time
  
  
# localtime() method used to
# get the object containing
# the local time.
Time = time.localtime()
  
# strftime() method used to
# create a string representing
# the current time.
currentTime = time.strftime("%H:%M:%S", Time)
print(currentTime)