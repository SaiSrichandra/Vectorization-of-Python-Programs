with open('file.txt') as f:
     
    while True:
         
        # Read from file
        c = f.read(5)
        if not c:
            break
 
        # print the character
        print(c)