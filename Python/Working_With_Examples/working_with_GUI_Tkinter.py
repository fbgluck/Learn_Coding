# Print Hello World to the screen
# Ref: https://realpython.com/python-gui-tkinter/
from tkinter import *

# This function is executed when the 
def buttonClicked():
    rootWindow.greeting.configure (
        text="I got clicked"
    )
    
#create the root window
rootWindow = Tk()
# Set the title of the window
rootWindow.title("Test Window")
rootWindow.geometry('250x500')
rootWindow.greeting = Label(
    text="Hello There",
    foreground = "white",
    background="purple",
    width=20,
    height=10

    )
rootWindow.button1 = Button(
    text="Click me!",
    width=10,
    height=2,
    bg="green",
    fg="black",
    command=buttonClicked # the name of the function when the button is clicked
    )

rootWindow.entry = Entry(
    rootWindow,
    fg="black",
    bg="yellow",
    width=50
    )
# Add widgets to the window
rootWindow.greeting.pack()
rootWindow.button1.pack()
#Place the focus (cursor) in the entry field
rootWindow.entry.focus_set()
rootWindow.entry.pack()
#get the item you entered in the entry field
itemName=rootWindow.entry
print (f'You entered {itemName}.')
#Display the Window and the widgets
rootWindow.mainloop()

