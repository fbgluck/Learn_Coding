<# What happens if you enter just a Return and no character. 
What is the length and what does the variable contain
#>
$userEntry = Read-host "Enter a number"
if ($userEntry.length -eq 0) { #the user just entered newLine
    write-host "You didn't enter anything"
    write-host "The entry is: $userEntry"
    write-host "The hex equivalent is: "
    $userEntry | Format-hex
}
else {
    write-host "You entered $UserEntry"
    write-host "The hex equivalent is: "
    $userEntry | Format-hex
}