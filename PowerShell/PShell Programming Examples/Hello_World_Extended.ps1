<# This is my first Power Shell Script
It doesn't do much, just prints some items out #>
#
# We will start with the programmers favorite  - Hello World
# ... but first, we will clear the screen
# Concepts: Host Output
# Concepts: Host Input
cls
Write-Host "hello world"
# And we will wait until the user enters the ENTER key
pause
$date = Get-Date # set the variable $date
$age = Read-Host "Please tell me how old you are?" # Write something to the console
Write-Host "You are" $age "years old" and today is $date # Now output it all
