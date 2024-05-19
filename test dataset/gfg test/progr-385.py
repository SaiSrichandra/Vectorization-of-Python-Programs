import re
  
# defining object file1 to open
# GeeksforGeeks file in read mode
file1 = open('GeeksforGeeks.txt',
           'r')
  
# defining object file2 to open 
# GeeksforGeeksUpdated file in
# write mode
file2 = open('GeeksforGeeksUpdated.txt','w')
  
# reading each line from original
# text file
for line in file1.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("^Geeks", line)
      
    if not x:
        
        # printing those lines
        print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file2.write(line)
          
# close and save the files
file1.close()
file2.close()