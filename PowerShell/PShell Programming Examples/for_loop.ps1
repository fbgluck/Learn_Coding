Clear-Host

# Use this to seperate output
$break_line = "+_+_+_+_+_+__+_+_+_+_+_+_+_"

<# Four parts to a for loop:
1. Declare and set the initial value of the counter
2. Define the test condition. The loop statements will execute as long as the statement evaluates to true.
3. Define the increment value of the counter ($counter++ is a shortcut for $counter = $counter + 1)
4. The statements which are enclosed between curly brackets. {   }

for <initial value>;<test condition>;<increment statement> { <loop statements> }


#>
$userInput = Read-Host "Enter the starting value for the loop"
$counter = [int]$userInput
for ($counter; $counter -le 10; $counter= $counter + 1) {
    write-host $counter
}
write-host $break_line
<#
While is a "pre-test" loop. The condition is tested before the loop is executed.
#>
$userInput = Read-Host "Countdown From What Number?..."
While ($userInput -ne 0) {
    Write-Host "Countdown from: " $userInput
    $UserInput = $UserInput - 1
}
write-host $break_line
<# do while is a post-test loop. The test is run after the loop statements
are executed. This means that statements in a do... while loop will always be executed at least once 
#>
$userInput = Read-Host "Do While Loop Starting Value: "
do {
    write-host "Loop test value is now: " $userInput
    $userInput = $userInput - 1
    }
while ($userInput -ge 0)
write-host $break_line
$userInput = Read-Host "Do Until Loop Starting Value: "
do {
    write-host "Loop test value is now: " $userInput
    $userInput = $userInput
}
until ($userInput -ge 0)
        