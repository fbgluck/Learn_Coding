# This code explains the use of Regular Expressions (Regex) in PowerShell
#ref: https://regex101.com/
$string = read-host "Enter A String with chacters only "
if ($string -match "[a-z][ ][a-z]") {
    Write-host "The String passes the test"
}
else {
    write-host "You entered:" $string
    write-host "This is not a legal string"
}
# Match a phone number
$phoneNumber = read-host "Enter a phone number:(ddd)-ddd-dddd"
if ($phoneNumber -match "[^(\d{3})\d{3}-\d{4}]") {
    write-host "You Entered " $phoneNumber "in the correct format"
}
else {
    write-host "Your phone number " $phoneNumber "is not in the correct format"
}

# Check to see if a filename matches the correct format