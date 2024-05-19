import time
import datetime
  
  
string = "20/01/2020"
  
element = datetime.datetime.strptime(string,"%d/%m/%Y")
  
tuple = element.timetuple()
timestamp = time.mktime(tuple)
  
print(timestamp)