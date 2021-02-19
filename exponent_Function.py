print(2**3)

# creating our own exponent function using for loop

def raise_to_power(base_num, pow_num): 
	result = 1
	for index in range(pow_num):
		result = result * base_num
	return result

print(raise_to_power(3,2))
#9
print(raise_to_power(2,4))
#16
