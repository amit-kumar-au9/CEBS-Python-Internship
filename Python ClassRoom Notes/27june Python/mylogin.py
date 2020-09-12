import tkinter as tk


root = tk.Tk()
root.wm_title("CEBS Login")
root.geometry("500x400")
root.wm_maxsize(600,600)
root.wm_minsize(300,300)
root.wm_resizable(0,0)

print(dir(root))

root.mainloop()