def readFile():
	try:
		file = open("stud.txt","r")
	except:
		file = open("stud.txt","w")
		file.close()
		print("OOPS!! file not exist")
		readFile()

readFile()