import mysql.connector as MySQL
conn = ""
cursor = ""
hostName = "localhost"
userName = "root"
password = ""
dataBase = "cebs"


def createConnection():
	global conn
	global cursor
	global hostName
	global userName
	global password
	global dataBase
	try:
		conn = MySQL.connect(host = hostName, user = userName,passwd = password,database = dataBase)
		cursor = conn.cursor()
	except Exception as e:
		print("OOPS cant create Connection ",e)


def userRegister():
	createConnection()
	global cursor
	fname = input("Enter First Name \t: ")
	lname = input("Enter Last Name \t: ")
	email = input("Enter Email \t\t: ")
	phone = input("Enter Phone \t\t: ")
	uname = input("Enter User Name \t: ")
	passw = input("Enter Password \t: ")
	SQL = "insert into user(fname,lname,email,phone,uname,password) values (%s,%s,%s,%s,%s,%s) "
	val = (fname,lname,email,phone,uname,passw)
	try:
		cursor.execute(SQL,val)
		print("User registered")
		conn.commit()
		conn.close()
	except:
		print("Sorry cant register")

	
def userLogin():
	createConnection()
	global cursor
	uname = input("Enter User Name \t: ")
	passw = input("Enter Password \t : ")
	SQL = "select * from user where uname = %s and password = %s "
	print("\n\n",SQL,"\n\n")
	val = (uname,passw)
	try:
		cursor.execute(SQL,val)
		result = cursor.fetchone()
		flag = 0
		for data in result:
			flag = 1
			print(data,end="\t")
		if flag == 0:
			print("Invalid uname/password")
		print()
		conn.close()
	except Exception as e:
		print("Error in SQL")

def main():
	while(True):
		print("\n\n1. User Register")
		print("2. User Login")
		print("0. Exit")
		choice  = int(input("Enter Choice : "))
		if choice == 1:
			userRegister()
		elif choice == 2:
			userLogin()
		elif choice == 0:
			print("Bye Bye")
			break
		else:
			print("Invalid Choice")


if __name__ == "__main__":
	main()
			
		