class WD:
	def __init__(self,capacity,size):
		self.capacity = capacity
		self.size = size

	def getHDDInfo(self):
		print("Information of WD HDD : ",self.capacity," GB, ",self.size," inch")


class SeaGate:
	def __init__(self,capacity,size):
		self.capacity = capacity
		self.size = size

	def getHDDInfo(self):
		print("Information of SeaGate HDD : ",self.capacity," GB, ",self.size," inch")


class I7:
	def __init__(self,ghz,core):
		self.ghz = ghz
		self.core = core
	def getCPUInfo(self):
		print("Information of CPU : ",self.ghz," GHZ",self.core," cores")

class I5:
	def __init__(self,ghz,core):
		self.ghz = ghz
		self.core = core
	def getCPUInfo(self):
		print("Information of CPU : ",self.ghz," GHZ",self.core," cores")

class I3:
	def __init__(self,ghz,core):
		self.ghz = ghz
		self.core = core
	def getCPUInfo(self):
		print("Information of CPU : ",self.ghz," GHZ",self.core," cores")



class Laptop:
	company = "samsung"	
	def __init__(self,hdd,cpu):
		self.hdd = hdd
		self.cpu = cpu

	def getLaptopInfo(self):			
		print(Laptop.company," laptop")
		self.hdd.getHDDInfo()
		self.cpu.getCPUInfo()


sg = SeaGate(1024,2.5)
cpu = I5(2.5,2)
l1 = Laptop(sg,cpu)

l1.getLaptopInfo()