from tkinter import *
from tkinter.filedialog import *
class Notepad(Frame):
	def __init__(self,master = None):
		self.master = master
		super().__init__(self.master)
		self.master.geometry("400x400")
		self.master.title("Notepad +++")
		self.master.wm_resizable(0,0)
		self.createGUI()

	def createGUI(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)
		fileMenu = Menu(self.master)
		fileMenu.add_command(label="New",command=self.new_file)
		fileMenu.add_command(label = "Open", command=self.open_file)
		fileMenu.add_command(label = "Save", command=self.save_file)
		fileMenu.add_command(label = "Save as", command=self.saveas_file)		
		menu.add_cascade(label="File",menu=fileMenu)
		
	def new_file(self):
		print("new File Created")
	def save_file(self):
		print("File save")
		asksaveasfile(initialdir="/",title="Save File",mode="r")
	def saveas_file(self):
		print("File Saved")
	def open_file(self):
		print("new File Opened")
		res = askopenfilename(initialdir="/",title="Select File",filetypes=(("python files","*.py"),("Text Files","*.txt"),("All files","*.*")))	
	

def main():
	root = Tk()
	notepad = Notepad(root)
	root.mainloop()



if __name__ == "__main__":
	main()