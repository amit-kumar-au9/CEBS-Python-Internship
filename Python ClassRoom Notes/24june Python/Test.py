#Polymorphism

	1) duck typing

	2) function overloading
	
	3) operator Overloading
	
	4) function Overriding


_______________________________________________________________
class WD:
	def __init__(self,capacity,size):
		self.capacity = capacity
		self.size = size

	def getHDDInfo(self):
		print("Information of WD HDD : ",self.capacity,", ",self.size)


class SeaGate:
	def __init__(self,capacity,size):
		self.capacity = capacity
		self.size = size

	def getHDDInfo(self):
		print("Information of SeaGate HDD : ",self.capacity,", ",self.size)



class Laptop:
	company = "samsung"	
	def __init__(self,hdd):
		self.hdd = hdd

	def getLaptopInfo(self):			
		print(Laptop.company," laptop")
		self.hdd.getHDDInfo()


wd = WD(1,2.5)
l1 = Laptop(wd)















