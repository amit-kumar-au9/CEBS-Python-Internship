from abc import ABC,abstractmethod

#3.4+

class My(ABC):
	@abstractmethod
	def sum(self):
		pass


class MyChild(My):
	def sum(self):
		print("Hello Python")


m = My()

m.sum()