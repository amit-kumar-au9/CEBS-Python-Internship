from tkinter import *
from threading import *
from socket import *

class MyClient(Thread):
	def createGUI(self,master=None):
		self.master = master
		self.socket_ = None
		self.master.title("CEBS Client")
		self.master.wm_geometry("400x400")
		self.master.wm_resizable(0,0)
		self.nameVar = StringVar()
		self.messageVar = StringVar()
		self.history = Text(self.master)
		sendBtn = Button(self.master,text="Send", command=self.sendMessage)
		nameTx = Entry(self.master,textvariable=self.nameVar)
		messageTx = Entry(self.master,textvariable=self.messageVar)
		nameTx.place(x=20,y=20,width=360,height=30)
		self.history.place(x=20,y=60,width=360,height=280)
		messageTx.place(x=20,y=350,width=300,height=30)
		sendBtn.place(x=330,y=350,width=50,height=30)
	def run(self):
		try:
			self.socket_ = socket()
			self.socket_.connect(('localhost',9454))
			self.history.insert(END,"**********************\nConnection with Server\n**********************\n")
			while True:
				print("hello client")
				msg = self.socket_.recv(1024)
				self.history.insert(END,msg)
		except Exception as e:
			print("Server Error : ",e)
	def sendMessage(self):
		print("send message from client")
		if self.socket_ != None:
			msg = self.nameVar.get() + " : " + self.messageVar.get()+"\n"
			self.history.insert(END,msg)
			self.socket_.send(msg.encode('utf-8'))
			self.messageVar.set('')
def main():
	tk = Tk()
	myClient = MyClient()
	myClient.createGUI(tk)
	myClient.start()
	tk.mainloop()

if __name__ == "__main__":
	main()