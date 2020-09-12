fileName = "student.txt"

def getLastStudentID():
	global fileName
	try:
		file = open(fileName,"r")
		listOfLines = file.readlines()
		lastRecord = listOfLines[len(listOfLines)-1]
		studentList = lastRecord.split(",")
		return int(studentList[0])+1
	except:
		file = open(fileName,"w")
		file.close()
		return 1

def addStudentRecord():
	print("***********************************************************")
	global fileName
	file = open(fileName,"a")
	id = getLastStudentID()
	name = input("Enter Student Name \t: ")
	email = input("Enter Student Email \t: ")
	phone = input("Enter Student Phone \t: ")
	mphy = int(input("Enter Student Marks(Physics) \t: "))
	mchm = int(input("Enter Student Marks(Chemistry) \t: "))
	mmath = int(input("Enter Student Marks(Maths) \t: "))
	file.write(str(id)+","+name+","+email+","+phone+","+str(mphy)+","+str(mchm)+","+str(mmath)+"\n")	
	file.close()
	print("\n Record Saved")
	print("***********************************************************")
def updateStudentRecord():
	global fileName
	file = open(fileName,"a")

def removeStudentRecord():
	pass

def deleteStudentRecord():
	pass

def searchStudentRecord():
	pass

def displayStudentRecord():
	print("ID\tName\tEmail\tPhone\tMarks(Phy/Chem/Math)")
	



def main():
	while True:
		print("1. Add Student Record")
		print("2. Update Student Record")
		print("3. Remove Student Record")
		print("4. Delete all Student Record")
		print("5. Search Student")
		print("6. Display Student Records")
		choice = int(input("Enter Choice : "))

		if choice == 1:
			addStudentRecord()
		elif choice == 2:
			updateStudentRecord()
		elif choice == 3:
			removeStudentRecord()
		elif choice == 4:
			deleteStudentRecord()
		elif choice == 5:
			searchStudentRecord()
		elif choice == 6:
			displayStudentRecord()
		elif choice == 0:
			print("Bye Bye")
			break
		else:
			print("\nInvalid Choice\n")
	
if __name__ == "__main__":
	main()