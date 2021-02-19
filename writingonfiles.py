 # be careful if you just use "w" it is going to erase whole file and write on it
python_employees_file = open("python_employees.txt", "a")
python_employees_file.write("Toby - Human Resources")  # adding to at the end of a file  but not in new line
python_employees_file.close()
#there is problem to run code probably because of sublime actially it is not. it was because file was open

python_employees_file = open("python_employees.txt", "a")
python_employees_file.write("\nKelly - Customer Service")  # \n adding to at the end of a file  but in a new line
python_employees_file.close()

python_employees_file = open("python_employees.txt", "r")
print(python_employees_file.readlines()) 
python_employees_file.close()


#python_employees_file = open("python_employees.txt", "w")
#python_employees_file.write("\nKelly - Customer Service")  # deleting whole file and ll rewrite on it
#python_employees_file.close()

# instead do this way create new file as below

python_employees_file = open("python_employees1.txt", "w")
python_employees_file.write("\nKelly - Customer Service")  # creating new text file you can name it as you want a.text etc
python_employees_file.close()
#Kelly - Customer Service  # good thing even i run code multiple times it doesnt create same file again and again

python_employees_file = open("index.html", "w")
python_employees_file.write("<p>This is HTML</p>")  # we can create different type of files too like html
python_employees_file.close()
'''This is HTML'''    # creating this website make me really excited

