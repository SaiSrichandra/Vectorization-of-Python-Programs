from datetime import datetime
  
  
timestamp = 1553367060
dt_obj = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
  
print("date:",dt_obj)