<#
Ref: https://www.itprotoday.com/powershell/powershell-goodbye-goto
The four basic PowerShell iteration statements (while, do while, do until, and for) all allow you to repeat code based on a conditional statement.
Use whichever of the four iteration statements make your code the clearest and easiest to read.
#>

Clear-Host # Clears screen
$verbosePreference = "Continue" # set option to continue after verbose message displayed (ref: PowerShell Preference Variables)
write-verbose -message "Program Starts at: $(get-date)" # How to display function along with message

#For loops -- testing done at the beginning
write-host "For Loop" -BackgroundColor red -foregroundcolor white
for ($loopCounter = 10;$loopCounter -gt 0; $LoopCounter--)
    {write-verbose "the counter is now: $loopCounter"}

# While Loop -- Testing done at the beginning
write-host "While Loop" -BackgroundColor red -foregroundcolor white
$loopCounter=10
While ($loopCounter -gt 0) {
    write-verbose "The counter is now: $loopCounter"
        $loopCounter--
}






# Do While -- testing is done at the end
write-host "Do While" -BackgroundColor red -foregroundcolor white
$marker = 10
do {
  write-verbose "The counter is now $marker"
  $marker--
} while ( $marker -gt 0 )


# DO Until -- testing is done at the end
$marker = 10
write-host "Do Until" -BackgroundColor red -foregroundcolor white
do {
    write-verbose "The counter is now $marker"
    $marker--
  } until ( $marker -gt 0 )