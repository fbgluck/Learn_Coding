# File Name: snippets.ps1
# Author: Fredric B. Gluck
# CNS 1
# ------------------------------------------------------------------------------------------#

#Snippet #1: This is a simple program to show math 
Clear-Host
$StartDate = Get-Date
Write-Host
Write-Host "Program Started at:" $StartDate.TimeOfDay -BackgroundColor red -ForegroundColor white
# File of snippets
# - show contents of windows logfile
# Get-WinEvent -LogName security -maxevents 10
#Sample variable use
# $count=1
# $count= $count + 1
# Write-Host "The value of the variable count is:  $count"

#---------------------------------------------------------------------------------------------#
# Snippet #2: This program check the day of the week and displays in class or remote depend on the day
# Construct: Conditionals

# step 1: get the day of the week and assign it to a variable
# Set variables
# $date=get-date # holds the get-date object
# $dow=$date.DayOfWeek # Yanks the day of the week from the date object
# write-host "Today is: $dow " -NoNewline # A test to see if we are getting the correct dow

# Step 2: Test the day of the week to determine what output should be written
# if ($dow -eq "Wednesday") {
#     Write-Host "and today Is A Remote Day" # Step 3; write the output
# }
# else {
#     Write-Host "and today is an in class day"
# }

# What is an approach to deal with Saturday and Sunday (the switch statement)

#-----------------------------------------------------------------------------------------
# Snippet #3 - Iterating over a set of objects with ForEach-Object
# Construct: Iteration
$numberOfAutomatics = 0  #set variables to a known value
write-host "The following services are started automatically:"
Get-service | Foreach-Object { # Each retrieved object is returned in a collection. This goes through each item in the collection
    if ($_.StartType -eq "Automatic") {
        $numberOfAutomatics++        
        write-host $NumberOfAutomatics ". " $_.DisplayName "start type is: " $_.StartType
    }
}
Write-Host "---------------------------------"
Write-host "There are $numberOfAutomatics" processes that start automatically
# ------------------------------------------------------------------------------------------
# Snippet #4 -
# Construct: For Loops
for ($counter = 1; $counter -le 100; $counter++ )
$factor = 4
for ($counter = 1; $counter -le 20; $counter++) {
        $result=$factor * $counter
        write-host $factor "*" $counter "=" $result
}

# This code shows the end time and how much time the code took to run
$EndDate = Get-Date
Write-Host "Program Ended at: " $EndDate.TimeOfDay -BackgroundColor red -ForegroundColor white
Write-Host "Total Runtime: " ($EndDate.TimeOfDay - $StartDate.TimeOfDay)