#MRO : Left to rigth
class GParent:
	def __init__(self):
		super().__init__()
		print("Grand parent const")

	def get1(self):
		print("GParent class get")

	def show1(self):
		print("GParent class show")

class Parent(GParent):
	def __init__(self):
		#GParent.__init__(self)
		super().__init__()
		print("parent const")
	
	def get2(self):
		print("Parent class get")

	def show2(self):
		print("Parent class show")


class Child(Parent):
	def __init__(self):
		#Parent.__init__(self)
		super().__init__()
		print("Child const")

	def get(self):
		super().get1()
		print("Child class get")

	def show(self):
		print("Child class show")

def main():
	c = Child()
	c.get()
if __name__ == "__main__":
	main()