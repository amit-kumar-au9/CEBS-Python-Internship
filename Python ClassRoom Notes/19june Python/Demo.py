class Demo:
	def show(self):
		self.a= 2020
		print("Hello Python OOPS")
		print(self.a) 

obj1 = Demo()

obj2 = Demo()

obj1.show()

Demo.show(obj2)

obj1.__setattr__('roll',12)

#print("Dict of class",obj1.__dict__)
print("dir of class",obj1.__dir__)

#print(obj2.roll)
#print(obj2)


#print(type(obj1))

print(dir(obj1))


