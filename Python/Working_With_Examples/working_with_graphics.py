# Ref: https://docs.python.org/3/library/tkinter.html
# Ref: https://www.tutorialspoint.com/python/python_gui_programming.htm
# Ref: https://docs.python.org/3/library/tk.html
from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("100x100")
def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()
