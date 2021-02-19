# I wake up
# If I'm hungry
#    I eat breakfast
# 
#I leave my house
#If it's cloudy
#    I bring an umbrella
#oterwise
#    I bring sunglasses

#I'm at the restaurant
#If I want meat 
#    I order steak
#otherwise if I want pasta
#    I order spaghetti & meatballs
#otherwise
#	 I order a salad.

is_male = True
if is_male:
	print("You are a male")
else:
	print("You are not a male")	



is_male = True
is_tall = True
if is_male or is_tall:
	print("You are a male or tall or both")
else:
	print("You are neither  male or tall")	


is_male = False
is_tall = False
if is_male or is_tall:
	print("You are a male or tall or both")
else:
	print("You are neither  male or tall")	


is_male = True
is_tall = True
if is_male and is_tall:
	print("You are a male and tall")
else:
	print("You are either not male or not tall or both")	
#You are a male and tall

is_male = True
is_tall = True
if is_male and is_tall:
	print("You are a male and tall")
elif is_male and not(is_tall):
	print("You are a short male")
elif not(is_male) and is_tall:
	print("You are tall and not male")
else:
	print("You are not male and not tall")




