import time
 
curr_time = time.strftime("%H:%M:%S", time.localtime())
 
print("Current Time is :", curr_time)
 
nano_seconds = time.time_ns()
 
print("Current time in Nano seconds is : ", nano_seconds)