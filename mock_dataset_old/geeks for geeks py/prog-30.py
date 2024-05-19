def check(string) :
 

    p = set(string)
 
    # declare set of '0', '1' .
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else :
        print("No")
 
 
         
# driver code
if __name__ == "__main__" :
 
    string = "101010000111"
 
    # function calling
    check(string)