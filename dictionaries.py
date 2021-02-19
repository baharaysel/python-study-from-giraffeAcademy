monthConversions = {
	"Jan" : "January",
	"Feb" : "Febuary",
	"Mar" : "March",
	"Apr" : "April",
	"May" : "May",
	"Jun" : "June",
	"Jul" : "July",
	"Aug" : "August",
	"Sep" : "September",
	"Oct" : "October",
	"Nov" : "November",
	"Dec" : "December",
	}

print(monthConversions["Nov"])
#November
print(monthConversions.get("Dec"))
#December
print(monthConversions.get("X"))
#none
print(monthConversions.get("X","Not a valid key"))
#Not a valid key


# We can use numbers instead of strings as well
monthConversions2 = {
	1 : "January",
	2 : "February",
	3 : "March",
	4 : "April",
	5 : "May",
	6 : "June",
	7 : "July",
	8 : "August",
	9 : "September",
	10 : "October",
	11 : "November",
	12 : "December",
	}

print(monthConversions2[2])
#February
print(monthConversions2.get(1))
#January
