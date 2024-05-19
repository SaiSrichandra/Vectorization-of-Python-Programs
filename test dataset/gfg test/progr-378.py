arr = []
 
# count number of
# lines in the file
line = 1
for word in read:
    if word == '\n':
        line += 1
print("Number of lines in file is: ", line)
 
for i in range(line):
    # readline() method,
    # reads one line at
    # a time
    arr.append(df.readline())