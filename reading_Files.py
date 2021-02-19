# Reading Files
# Reading from external files like text file, csp, html
#opening, reading, closing

#open("python_employees.txt", "r")   # to read file
#open("python_employees.txt", "w")   # to write on file
#open("python_employees.txt", "r+")   # to read and write on file
#open("python_employees.txt", "a")   # to append on information on end of file. you cant change information but you can add

#python_employees_file = open("python_employees.txt", "r")
#print(python_employees_file.readable())
#python_employees_file.close()  # always good practice to close the file after you are done
#...True  because file is open and readable

python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.read())
python_employees_file.close()
#Jim -  Salesperson
#Dwight – Salesperson
#Pam – Receptionist
#Michael – Manager
#Oscar – Accountant

python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.readline())  # it reads only first line
python_employees_file.close()
#Jim - Salesperson

python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.readline())
print(python_employees_file.readline()) # it will read second line after first line
python_employees_file.close()
#Jim -  Salesperson
#Dwight – Salesperson


python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.readlines())   # read lines in the list    not readline readlines
python_employees_file.close()
#['Jim -  Salesperson\n', 'Dwight – Salesperson\n', 'Pam – Receptionist\n', 'Michael – Manager\n', 'Oscar – Accountant\n', '\n']


python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.readlines()[1])   # read line in the list in second index
python_employees_file.close()
#Dwight – Salesperson

python_employees_file = open("python_employees.txt", "r")
for employee in python_employees_file.readlines():
	print(employee)
python_employees_file.close()
# it prints all employees

