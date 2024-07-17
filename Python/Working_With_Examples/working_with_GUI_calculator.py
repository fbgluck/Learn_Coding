# working_with_GUI_calculator
# An attempt to make a GUI calculator
import customtkinter

numstring=""


# Define function to perform operation on two operators
def numberButtonPressed(numPressed):
    global numstring
    answer.delete('1.0','end') # Clear the field in prep for the modified string
    numstring=numstring + numPressed #add the next number onto the string
    answer.insert("end",numstring) #place the new string into the textbox at the end of the contents 

# def mathOpPressed(operation):

# Define GUI
# start by setting up root window object
rootWin = customtkinter.CTk() # root window object
rootWin.geometry("500x400")
rootWin.title("Calculator")

# Frame for buttons
frmButton = customtkinter.CTkFrame(master=rootWin, width=20, height = 100  )
frmButton.configure(fg_color='yellow')
frmButton.grid(row=1, column=1, padx=4,)

# Styles
# customtkinter.set_default_color_theme("path/to/your/custom_theme.json")


# Add a text widget for the answer under root window
answer = customtkinter.CTkTextbox(master = rootWin, width = 480, height = 20,)
# Place The Answer text widget
answer.grid(row=0,column=0, padx=4, pady=4,columnspan=5, )

# Create the tape widgit for the paper tape
tape = customtkinter.CTkTextbox(master=rootWin, width=200, height=200)
# Place the tape widit 
tape.grid(row=1,column=0, padx=4,pady=4,rowspan=4)

# Create the math function buttons
btnPlus=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "+")
btnPlus.grid(row=1,column=1,padx=4,pady=4)

btnMinus=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "-")
btnMinus.grid(row=2,column=1,padx=4,pady=4)

btnTimes=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "*")
btnTimes.grid(row=3,column=1,padx=4,pady=4)

btnDivide=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "/")
btnDivide.grid(row=4,column=1,padx=4,pady=4)

#Create the number buttons
btnNo7=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "7",command=lambda: numberButtonPressed("7"))
btnNo7.grid(row=1,column=2,padx=4,pady=4)

btnNo8=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "8",command=lambda: numberButtonPressed("8"))
btnNo8.grid(row=1,column=3,padx=4,pady=4)
 
btnNo9=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "9",command=lambda: numberButtonPressed("9"))
btnNo9.grid(row=1,column=4,padx=4,pady=4)

btnNo4=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "4")
btnNo4.grid(row=2,column=2,padx=4,pady=4)

btnNo5=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "5")
btnNo5.grid(row=2,column=3,padx=4,pady=4)

btnNo6=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "6")
btnNo6.grid(row=2,column=4,padx=4,pady=4)

btnNo1=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "1")
btnNo1.grid(row=3,column=2,padx=4,pady=4)

btnNo2=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "2")
btnNo2.grid(row=3,column=3,padx=4,pady=4)

btnNo3=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "3")
btnNo3.grid(row=3,column=4,padx=4,pady=4)

btnNo0=customtkinter.CTkButton(master = frmButton, width=40, height=40,text = "0")
btnNo0.grid(row=4,column=3,padx=4,pady=4)

btnEqual=customtkinter.CTkButton(master = frmButton, width=40, height=180,text = "=")
btnEqual.configure(fg_color='red',bg_color="yellow")
btnEqual.grid(row=1,column=6,rowspan=4, padx=4,pady=4,sticky="N")


# ********* Program Starts Here *******************

# start the TKinter main loop
rootWin.mainloop()
#
print(f"Program Ends...")