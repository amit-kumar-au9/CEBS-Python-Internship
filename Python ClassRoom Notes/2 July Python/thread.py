#Threading in Python
from threading import *
from time import *
class Rabbit(Thread):
	def run(self):
		print("Rabbit start first")
		for i in range(0,100):
			sleep(0.1)
			print("Rabbit running and its step : ",i)
		print("Race finished for rabbit")

class Tortoise(Thread):
	def run(self):
		print("Tortoise start first")
		for i in range(0,100):
			sleep(0.1)
			print("Tortoise running and its step : ",i)
		print("Race finished for tortoise")

def main():
	harshit = Rabbit()
	ishna = Tortoise()
	harshit.start()
	ishna.start()
	print("Main thread started")
	for i in range(0,10):
		print("main",i)
	ishna.join()
	harshit.join()
	print("Main thread dead")


if __name__ == "__main__":
	main()