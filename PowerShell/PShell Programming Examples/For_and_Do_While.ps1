# File Name: For_and_Do_While.ps1
# Author: Fredric Gluck
# Date: 2/25/2021
# Concept: Loops and Repitition
# Concept: For Loop
# Concept: Do While
# This program illustrates how to use a for loop by printing multiplication
# tables for an integer that the user has entered
#
$break_line = "-----------------" # use this to separate output
$input = read-host -prompt "Enter an integer" # ask the user for input
$int_input = [int]$input #try an convert the string input to an integer
for ($counter = 1; $counter -le 10; $counter++) {
   # write the table and execute the math to print the result
   write-host $int_input "times" $counter "=" ($int_input * $counter) #don't forget.. math must be in ( and )
   }

Write-Host $break_line
Write-Host "Demonstration of a Countdown Loop starting at " $int_input
write-Host $break_line

# Now we do a simple countdown loop

$counter= $int_input; # set the initial value of the counter to the number input
do { #
    write-host "The value is now: " $counter
    $counter = ($counter - 1)
}
while ($counter -ge 0)
write-host "We have ignition..... and Lift Off"