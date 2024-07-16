#Clear-Host
# working_with_strings
# Strings are always objects in Powershell. Therefor you operate on them using methods
# You can see the methods available using get-member
# $string1 | get-member
$stringPointer = 0
$string1 = "abcdef"
$string2 = "ghijkl"
$reversedString=""

$stringLength = $string1.Length
Write-host $string1 has a length of $stringLength -BackgroundColor red -ForegroundColor white
#The first position of a string is position 0
Write-host The 2 characters starting at position 3 are: $string1.Substring(3,2) -BackgroundColor red -ForegroundColor white
#reverse string

for ($stringPointer = $stringLength; $stringPointer -ge 0; $stringPointer--) {
    write-host "in loop -- stringponter: $stringpointer"
    $nextCharacter = $string1.Substring($StringPointer,1)
    $reversedString = $reversedstring + $nextCharacter 
    write-host $reversedString
}
write-host "Done..."