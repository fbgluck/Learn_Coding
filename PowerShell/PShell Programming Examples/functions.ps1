<# 
<TOPIC> Functions </TOPIC>

#>
#--------------------------------------------------
# Define Functions For This Program
function Write-Greeting {
    $firstName = Read-Host "Enter your first name"
    $LastName = Read-Host "Enter the last name"
    $result = "Hello " + $firstName + " " + $LastName
    Write-Host Greeting: $result 
}

# This function takes parameters
function Write-BetterGreeting {
    param ([string]$FirstName, [string]$LastName, [int]$count)
    $result = "Hello " + $firstName + " " + $LastName
    Write-Host Greeting: $result -BackgroundColor blue -ForegroundColor white
}

# ------- Program Begins Here ------------------
# Call the first function (no parameters)
Write-Greeting
$firstNameInput = read-host "What is your first name?"
Write-BetterGreeting $firstNameInput Gluck
Write-BetterGreeting Robert Ross
Write-BetterGreeting Joe Smith 3
<#
<ASSIGNMENT>
 Can you write two functions (and one challenge):
    1. Writes a set of 10 file names beginning with file_0.txt
    and ending with file_10.txt
    
    2. Writes a set of 10 file names beginning with file_<n>.txt and ending
    with file_<n+10>.txt then calls the function with a different 
    beginning file number
        
    3.Write a function to convert a Fahrenheit temperate to Celsius
    and a second function to do the opposite. The functions can be very
    simple with a single parameter for the value to convert. 
    You don’t need to worry about passing values from the pipeline, 
    error handling or anything advanced. The function can simply 
    write the converted value to the pipeline as a result. 
    If you are feeling a bit more confident, have your function write an 
    object to the pipeline with the original and converted values. 
    (ref: https://ironscripter.us/a-beginner-powershell-function-challenge/ )
</ASSIGNMENT>
#>
