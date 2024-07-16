# Building UIs with CustomTKinter
# pip install customtkinter
# Documentation: https://customtkinter.tomschimansky.com/documentation/color
import customtkinter


# functions that are connected to a button
def process_action():
    print("Processing action code goes here")
    print(f"Your student number is {studentNumber.get()} ")
    studentNumber.delete(0,'end') # deletes the contents from the beginning to the end of the string

# ********** END OF FUNCTION DEFINITIONS


# Sets up GUI global specs
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")


# start by setting up root window object
root = customtkinter.CTk() # root window object
root.title="Check IN / Check Out"
root.geometry("500x400")

# Add a frame under a the root window
frame = customtkinter.CTkFrame( # creates a frame where the master of this element is root
    master=root,
    border_width=3
) 

# The Tkinter Geometry Manager places widgets onto the window at specific positions
# ref: https://www.geeksforgeeks.org/python-gui-tkinter/#geometry-management

# This calls the pack() geometry manager which places objects into blocks
# and then places them into the frame
frame.pack(padx=20, pady=60, fill="both", expand = True) 

# There is also the grid() geometry manager
# This is the one that is recommended
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

# and the place() method

# NOTE: All items in a frame must use the same geometry manager


# Add a label in the frame
# We will take care of the font first.
# Ref: https://www.youtube.com/@TkinterPython
# Ref: https://www.youtube.com/watch?v=bK9Xxa_nkO8

# Create an object that contains the font specs we will use for the title.
# Ref: https://customtkinter.tomschimansky.com/documentation/utility-classes/font
# This is a good method because the font can be applied to multiple wigits and
# it can be changed on the fly using the .configure method.

fontTitle = customtkinter.CTkFont(
    family = "Robotext",
    size=44,
    weight="bold",
    underline=True
)

lblTitle = customtkinter.CTkLabel(
    master=frame, 
    text="CheckIN / CheckOUT",
    padx=10,
    pady=12,
    font=fontTitle #Use the font object we defined above
    # font=("Roboto",24) # alternate way specify font and size
)
lblTitle.pack(padx=10,pady=12,fill="both",expand="True")

# Add an entryfield in the frame
studentNumber = customtkinter.CTkEntry(
    master=frame,
    placeholder_text="Student Number"
)
# organize this widgit into a block and place it into the parent
studentNumber.pack(padx=10,pady=12)
 
#Add an action button
btnGo=customtkinter.CTkButton(
    master=frame, #the parent for the button
    text="GO", # the text in the buttom
    command=process_action # The function to be executed when the button is clicked
)
#btnGo.grid(row=1,column=0,padx=10,pady=12 )
btnGo.pack(padx=10,pady=12)

# Add the Quit button. Destroys the main window
btnQuit=customtkinter.CTkButton(
    master=frame,
    text="Quit",
    command=root.destroy
    )
btnQuit.pack(padx=10,pady=10)



# ********* Program Starts Here *******************

# start the TKinter main loop
root.mainloop()
#
print(f"Program Ends...")