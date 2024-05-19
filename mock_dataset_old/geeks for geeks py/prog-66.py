def BinaryToDecimal(binary):
		
	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return (decimal)

# Driver's code
# initializing binary data
bin_data ='10001111100101110010111010111110011'

# print binary data
print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data
str_data =' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
	str_data = str_data + chr(decimal_data)

# printing the result
print("The Binary value after string conversion is:",str_data)