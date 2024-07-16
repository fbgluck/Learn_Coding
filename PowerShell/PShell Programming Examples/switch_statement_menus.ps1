<#
Program Name: Switch Statement
Program Author: Fredric Gluck
Description: This program demonstrates how to use the switch
statement to display a menu that allows users to select a choice
#>

#Demonstration of PS Switch statement that can be used for menus

$Process_Choice = $True # Flag to indicate valid choice was made

while ($Process_Choice) { #indicates that choice made is valid
    #Display the menu and ask for a selection
    Write-host " --------- MENU ----------"
    Write-host "1. First Choice"
    write-host "2. Second Choice"
    Write-host "Q. Quit Program"
    write-host
    $menuChoice = Read-Host "Make a choice or use 'q' to quit the program"

    #Check to see what the user wants to do
    if ($menuChoice -eq "q") {
    
        #Quit The Program by setting the flag to false
        $Process_choice = $false
        write-host "Quitting the Program..."
    }


#This gets done only if q was not entered and a valid selection was made
    if ($Process_choice) {

        Switch ($menuChoice) {
            1 {Write-Host "*** You chose 1"
                $Process_Choice=$false
                # Put additional code for choice 1 here
                Break
               }
            2 {Write-Host "*** You chose 2"
                #Put additional code for choice 2 here
                $Process_Choice = $false
                Break
              }
            Default {Write-host "That was not a valid choice"}
        }
    }
}
write-host "Program Done"