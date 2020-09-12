#MRO : Left to rigth
class Parent1:
	def get(self):
		print("Parent1 class get")

	def show(self):
		print("Parent1 class show")

class Parent2:
	def get(self):
		print("Parent2 class get")

	def show(self):
		print("Parent2 class show")


class Child(Parent2,Parent1):
	def get1(self):
		print("Child class get")

	def show1(self):
		print("Child class show")

def main():
	c = Child()
	print(dir(c))
	c.get()

if __name__ == "__main__":
	main()