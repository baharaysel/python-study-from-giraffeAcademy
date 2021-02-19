#Giraffe Language
#vowels -> g
#dog -> dgg
#cat -> cgt

def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter in "AEIOaeiou":
			translation = translation + "g"
		else:
			translation = translation + letter
	return translation

print(translate("Aysel is so smart"))
#gysgl gs sg smgrt
print(translate("Dog"))
#Dgg

print(translate(input("Enter a phrase: ")))
#Enter a phrase: Aysel
#gysel

def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter.lower() in "aeiou":
			if letter.isupper():
				translation = translation + "G"
			else:
				translation = translation + "g"
		else:
			translate = translation + letter
	return translation

print(translate(input("Enter a phrase: ")))

#Enter a phrase: G0L
#GGL




	