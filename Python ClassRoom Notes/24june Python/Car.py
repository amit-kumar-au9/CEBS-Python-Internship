#constructor : 
class Car:
	 
	def __init__(self):
		self.engine = 0
		self.name = ""
		self.color = ""
		self.model = ""
		self.price = 0

	def setAuto(self,isAuto):
		self.isAuto = isAuto

	def setSunRoof(self,isSunRoof):
		self.isSunRoof = isSunRoof

def main():

	swift = Car()
	altis = Car()
	altis.setAuto(True)
	altis.setSunRoof(False)

	print(dir(swift))
	print(dir(altis))		

if __name__ == "__main__":
	main()