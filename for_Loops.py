for letter in "Giraffe Academy":
	print(letter)


friends = ["Figen", "Birgul", "Esra"]
for friend in friends:
	print(friend)
# Figen
# Birgul
# Esra

friends = ["Figen", "Birgul", "Esra"]
for index in range(10):   # 10 is not included
	print(index)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

friends = ["Figen", "Birgul", "Esra"]
for index in range(3, 6):  # 6 is not included
	print(index)
#3
#4
#5

friends = ["Figen", "Birgul", "Esra"]
for index in range(len(friends)):
	print(friends[index])
#Figen
#Birgul
#Esra

friends = ["Figen", "Birgul", "Esra"]
for index in range(len(friends)):
	if index == 0:
		print("first Iteration")
	else:
		print("Not first")