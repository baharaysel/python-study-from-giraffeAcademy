def max_num(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else: 
		return num3

print (max_num(-6,-5,-1))
# !=  not equal

# also we can use for string to see if they are equal.   if "dog" == "cat"   etc .
print (max_num(-5,-7,3))

