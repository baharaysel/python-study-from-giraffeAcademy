friends = ["Aysel", "Furkan", "Ayse"]
print(friends)
friends = ["Aysel", "Furkan", "Ayse"]
print(friends[0])
friends = ["Aysel", "Furkan", "Ayse"]
print(friends[-1])
friends = ["Aysel", "Furkan", "Ayse"]
print(friends[1:])
friends = ["Aysel", "Furkan", "Ayse", "Ali", "get lost"]
friends[-1]= "Fatma" #modifying last value of the list
print(friends[-1])

# List Functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Aysel", "Furkan", "Ayse", "Ali", "Fatma"]
print(friends,lucky_numbers)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma'] [4, 8, 15, 16, 23, 42]

friends.extend(lucky_numbers)
print(friends)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 23, 42]
friends.append("Mustafa")
print(friends)
['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 23, 42, 'Mustafa']

friends.remove("Mustafa")
print(friends)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 23, 42]

friends.remove(23)
print(friends)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4 , 8, 15, 16, 42]


friends.insert(-1, "Abdulrezzak")
print(friends)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 'Abdulrezzak', 42]       #there is a problem. how can i give last position

friends.pop()
print(friends)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 'Abdulrezzak']   (it removes last element)


print(friends.index(15))
#7    it tells whoch index number 15 is. 

#print(friends.index("palabiyik"))
#because it is not in the list it gives error

friends=['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 'Abdulrezzak']
friends2 = friends.copy()
print(friends2)
#['Aysel', 'Furkan', 'Ayse', 'Ali', 'Fatma', 4, 8, 15, 16, 'Abdulrezzak']










friends.clear()
print(friends)
#[]

