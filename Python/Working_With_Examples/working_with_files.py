#! /usr/bin/python
# File I/O --
# ref: https://www.tutorialspoint.com/python/python_files_io.htm
""" Demonstrates how to open, close, read and write files"""
from datetime import date, datetime
import os  # This library lets interface with the OS
os.system("cls")  # Use the .system method with cls to Windows -- Clear output
print("---- PROGRAM STARTS -----")
# Define needed Variables:
stop_flag = False  # Used to indicate if user want to execute code

# get the current time and date
now_time = datetime.now()
print(f"*** Program Starts at {now_time}")

# define the name of the logfile. Note the \\
logfileName = ".\\logfiles\\logfile.txt"
# Check to see if logfile exists
if not (os.path.isfile(logfileName)):
    # Tell the user that the file does not exist
    print(f'{logfileName} does not exist... Should I create it?')
    file_answer = str.lower(input("Enter Y (default) or N:"))
    if file_answer == "" or file_answer == "y":
        stop_flag = False
    elif file_answer == "n":  # User wants to stop the file
        stop_flag = True
    else:
        stop_flag = True
        print("You need to enter either Y or N")
# If file does not exist, file will be created
# Open the file for writing
if not (stop_flag):  # We do not want to stop the program
    obj_workingfile = open(logfileName, "w")
    print(f"*** File " + obj_workingfile.name +
          " has been opened in mode: " + obj_workingfile.mode)

    # Alternate code to check for existing file
    # try:
    #    obj_workingfile = open("logfile.txt", "w")
    # except:
    # Open failed, so we assume that the file does not exist
    # and we will create it

    # Write one line to the file
    # Write does not automatically add newlines
    print(f"*** Writing The File")
    obj_workingfile.write("<<<Logfile started at:" + str(now_time) + ">>>\n")
    obj_workingfile.write(str(datetime.now()) +
                          " :: This is the second line of the file")
    # Close the open file -- it's important you do this!
    print(f"*** File Written... Closing the file")
    obj_workingfile.close()
    print(f"*** Reading The Entire File .....")
    # Reading Files
    obj_workingfile = open(logfileName, "r")
    # () contains the number of bytes (characters) to be read
    # if omitted, it reads as much as it can - most likely to the
    # end of the file.
    items_read = obj_workingfile.read()
    print(f"*** Read the following:\n{items_read}")
    obj_workingfile.close()
    print(f"-"*30)
    # Sample read the file line by line
    print(f"*** Reading the File Line By Line")
    obj_workingfile = open(logfileName, "r")
    # Read to EOF
    # If file.read() returns an empty str, it is the EOF.
    line_no = 0  # No lines have been read
    eof_reached = False  # used to indicate when EOF reached

    while not (eof_reached):  # check to see if EOF reached
        line_read = obj_workingfile.readline()  # Read one line
        if line_read != "":  # line read is not empty
            line_no += 1  # one more line was read
            print(f"<Line {line_no}>: {line_read}", end="")
        else:  # Line is "" (EOF Reached)
            eof_reached = True
            print(f"\n*** EOF Reached after {line_no} lines...")
    print(f"*** Closing the file...")
    obj_workingfile.close()
print("*** Program completed......")
