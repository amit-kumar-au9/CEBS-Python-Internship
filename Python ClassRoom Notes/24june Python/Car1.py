class Car:
	company = "suzuki"
	def __init__(self,engine,name,color,model,price):
		self.engine = engine
		self.name = name
		self.model = model
		self.color = color
		self.price = price

	def getCarDetails(self):
		print("Engine : ",self.engine)
		print("Name : ",self.name)
		print("Color : ",self.color)
		print("price : ",self.price)
		print("Model : ",self.model)
	
	@classmethod
	def getCompany(cls):
		print("company : ",cls.company)

	@staticmethod
	def getClassInfo():
		print("Car class Information")
	
def main():
	swift = Car(1300,"Swift","White","VXI",720000)
	swift.getCarDetails()

	city = Car(1600,"City","white","SX",1130000)
	city.getCarDetails()

	Car.getCompany()

	Car.company = "maruti";

	Car.getCompany()

	swift.getClassInfo()

if __name__ == "__main__":
	main()

