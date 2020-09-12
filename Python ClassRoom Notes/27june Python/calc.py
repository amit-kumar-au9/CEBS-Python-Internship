class Car:
	def __init__(self,engine,name,color,model,price):
		self.engine = engine
		self.name = name
		self.model = model
		self.color = color
		self.price = price

	def __gt__(self,other):
		if self.engine > other.engine:
			return True
		else:
			return False

swift = Car(1300,"swift","white","VXI",630000)

ciaz = Car(1496,"Ciaz","White","VDI",1130000)

if swift>ciaz:
	print("swift more powerfull")
else:
	print("ciaz more powerful")