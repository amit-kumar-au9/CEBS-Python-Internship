import tkinter as tk


root = tk.Tk()

imageObj = tk.PhotoImage(file="abc.gif")

button = tk.Button(root,image=imageObj)
button.pack()

root.mainloop()