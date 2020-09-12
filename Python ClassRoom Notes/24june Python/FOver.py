#function Overloading

class FOver:
	def show(self):
		print("Show1")	
	def show(self,a):
		print("show2")
	def show(self,a,b):
		print("show3")


o = FOver()	