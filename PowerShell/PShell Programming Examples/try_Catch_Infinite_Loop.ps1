# This Program checks for proper input using Try Catch Error checking
# Concepts: Try Catch
# Concepts: If Then Else
# try and catch are always a pair
#  - catch is executed when the statements in try throw an error
# ---------------------------------------------------------------------------------#
#use $numOK to determine if input was valid and we will execute the times tables
# ref: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables?view=powershell-7.2
$numOK=$true #Flag to indicate that the input could be converted to an integer
$continueExecution = $true # flag used to exit the program
while ($continueExecution) {

    $userInput = read-host -prompt "Enter an integer or Q to quit"
    #Check to see if user wants to stop the program
    if (($userInput -eq "Q") -or ($userInput -eq "q")) {
        $continueExecution = $false # set the flag to stop the program
        $numOK = $false # A number was not entered
    }
    else {
        try {
            $userInput = [int]$userInput #try an convert the string input to an integer
            $numOK = $true
            Write-Host "You entered the number: " $userInput
        } # end try
        catch {
            write-host "Sorry, you must enter a number. You entered $userInput"
            $numOK=$false
        } #end catch
    } # end else

   
    # Execute this if the input was a valid integer and the program is to be continued
    if (($numOK) -and ($continueExecution)) { 
        for ($counter = 1; $counter -le 10; $counter++) {
            # write the table and execute the math to print the result
            write-host $userInput "times" $counter "=" ($userInput * $counter) #don't forget.. math must be in ( and )
        }
    }
    else{    
        if ($continueExecution) {
            $shouldWeContinue = read-host "Enter Y to try again or any other character to stop the program"
            if ($shouldWeContinue -ne "Y") {
                $continueExecution=$false
            }
            else {
                $continueExecution = $true # User wants to try again
            }
            }
        }
    } #end of while loop
# And terminate the program
Write-Host "Program complete"