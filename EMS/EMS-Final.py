import json

with open('file.txt') as json_file:
    users = json.load(json_file)

def save():
 with open('file.txt', 'w') as file:
     file.write(json.dumps(users))

def userInput():
    employeeName = input("Enter your name: " )
    employeeSSN = int(input("Enter your Social Security Number: " ))
    employeePhone = input("Enter your phone number, 10 digits with no spaces : " )
    pref = employeePhone[0:3]
    post = employeePhone[3:10]
    phonePretty = "("+pref+")"+post
    employeeEmail = input("Enter your email address: " )
    employeeSalary = float(input("Enter your total salary for the year: " ))
    salaryPretty = "$"+format(employeeSalary, ",.2f")

    users.append({
		'Name': employeeName,
		'SSN': employeeSSN,
        'Phone': phonePretty,
        'Email': employeeEmail,
        'Salary': salaryPretty
	    })
    save()
    print ("New User Successfully Entered")


def userShow():
	userNum = len(users)
	for i in range(userNum):
          print(28*'-',users[i]['Name'],28*'-')
          print(28*' ','SSN: ',users[i]['SSN'])
          print(28*' ','Phone: ',users[i]['Phone'])
          print(28*' ','Email: ',users[i]['Email'])
          print(28*' ','Salary: ',users[i]['Salary'])
          print(72*'-')
	print("There are",userNum,"users in the system.")

def userPick():
    print("Search by SSN: ")
    searchNum = int(input("Enter the user's SSN: " ))
    for x  in  users:
        if (searchNum == x['SSN']):
            atUser = users.index(x)
            print('\n','User',atUser)
            print(28*'-',users[atUser]['Name'],28*'-')
            print(28*' ','SSN: ',users[atUser]['SSN'])
            print(28*' ','Phone: ',users[atUser]['Phone'])
            print(28*' ','Email: ',users[atUser]['Email'])
            print(28*' ','Salary: ',users[atUser]['Salary'])
            print(72*'-','\n')

    userEdit = int(input("to edit the user's information, select the following, 1=Name, 2=SSN, 3=Phone, 4=Email, 5=Salary, 6 to exit user editing: "))
    if (userEdit == 1):
        newName = input("Enter your name: " )
        users[atUser]['Name'] = newName
        print('\n',users[atUser],'Name updated.','\n')

    elif(userEdit == 2):
        newSSN = int(input("Enter your Social Security Number: " ))
        users[atUser]['SSN'] = newSSN
        print('\n',users[atUser],'SSN updated.','\n')

    elif(userEdit == 3):
        newPhone = input("Enter your phone number: " )
        users[atUser]['Phone'] = newPhone
        print('\n',users[atUser],'Phone updated.','\n')

    elif(userEdit == 4):
        newEmail = input("Enter your email address: " )
        users[atUser]['Email'] = newEmail
        print('\n',users[atUser],'Email updated.','\n')

    elif(userEdit == 5):
        newSalary = float(input("Enter your total salary for the year: " ))
        users[atUser]['Salary'] = newSalary
        print('\n',users[atUser],'Salary updated.','\n')

    elif(userEdit == 6):
        print('Ok')

print("\n" * 4)
print("----------Welcome to the Employee Management System----------")
print("\n")
userNumb = len(users)
print("There are (",userNumb,") users in the system.")
print("\n")
print("-" * 61)
print("\n")
print(" 1) Enter a new user","\n","2) View all Users","\n","3) Pick and edit a user","\n","4) Exit")

dec1 = int(input("Please enter your option number: "))

while dec1 == 1 or 2 or 3 or 4:
 if dec1 == 1:
  userInput()
  save()
 elif dec1 == 2:
  userShow()
 elif dec1 == 3:
  userPick()
  save()
 elif dec1 == 4:
  break
 dec1 = int(input("Select '1' to enter a new user, '2' to view all users, '3' to pick and edit a user, or '4' to exit: "))


print("Thank you for using the EMS.")
