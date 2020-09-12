from tkinter import *
from threading import *
from socket import *

class MyServer(Thread):
	def createGUI(self,master=None):
		self.master = master
		self.client = None
		self.master.title("CEBS Server")
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
			self.socket_.bind(('',9454))
			self.history.insert(END,"**********************\nServer Started\n**********************\n")
			self.socket_.listen()
			self.history.insert(END,"Open to connect with Client\n**********************\n")
			client , addr = self.socket_.accept()
			self.client = client
			self.history.insert(END,"One Client Connected\n**********************\n")
			while True:
				print("hello server")
				msg = self.client.recv(1024)
				self.history.insert(END,msg)
		except Exception as e:
			print("Server Error : ",e)
	
	def sendMessage(self):
		print("send message from server")
		if self.client != None:
			msg = self.nameVar.get() + " : " + self.messageVar.get()+"\n"
			self.history.insert(END,msg)
			self.messageVar.set('')
			self.client.send(msg.encode('utf-8'))
def main():
	tk = Tk()
	myServer = MyServer()
	myServer.createGUI(tk)
	myServer.start()
	tk.mainloop()

if __name__ == "__main__":
	main()