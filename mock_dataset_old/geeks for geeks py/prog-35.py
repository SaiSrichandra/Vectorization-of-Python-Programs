
def Replace(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1
     
string = "14, 625, 498.002"
print(Replace(string))