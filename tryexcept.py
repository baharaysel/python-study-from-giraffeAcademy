
try:
	number = int(input("Enter a number: "))
	print(number)
except:
	print("Invalid Input")


# trying to catch different type of errors

try:
	value = 10 / 0
	number = int(input("Enter a number: "))
	print(number)
except ZeroDivisionError:
	print("Divide by zero")
except ValueError:
	print("Invalid Input")
# it didnt work it gives error


# saving Error as variable

try:
	answer = 10/0
	number = int(input("Enter a number: "))
	print(number)
except ZeroDivisionError as err:
	print(err)
except ValueError:
	print("Invalid Input")
#division by zero

#try:     
#except:
# dont leave except empty it is not good practice . We want to know catch the specific type of error.


		