def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            print(i+1, end=", ")
 
 
findline("Hello")