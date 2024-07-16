# "hello world" | get-member  << Use this so show Methods and Properties of strings
# ------------------------------------- #

# ----- String Length ------------------#
$testString = [string]"abcdefghi"
#[int]$stringLength = $testString.Length
#Write-Host "The string $testString is $stringLength characters long" -ForegroundColor white -BackgroundColor Blue

# Position of one string in another
#$position = $testString.IndexOf("d")
#write-host "The Index of d is: $position"

# ----------------------One String Contained In Another--------------------------#

# $testChar =  Read-Host -Prompt "Enter a Single Character:"
#     if ($testString.Contains,"$testChar") {
#         write-host "$testChar is not contained in $testString" 
# }   else {
#         write-host "$testChar is contained in $testString"
# } # ------------ Concatination -----------------------#
# Write-Host
# $lastName = "Ross"
# $firstName = "Bob"
# $fullName = $firstName + ' ' + $lastName
# Write-Host "Welcome to:" $fullName

# How would you pick the file name from this
# $fullFilePath = C:\users\fgluck\students.txt

# Output to the console a list of files named "file_1.txt" to "file_25.txt"
# Items to be used: for_loop and concatenation

# for ($num = 1; $num -le 25; $num++) {
# 	 $fileName = "file_" + $num + ".txt"
# 	 write-host $fileName
# }

# # Change a string from Mixed Case to all lower case (useful for input testing)
# $answer = Read-Host "Enter Yes or No"
# $answer = $answer.ToLower
# if ($answer -eq "yes") {
# 	Write-Host $answer

# }

# trim the * Characters from the beginning and end of this string:
$trimTarget = "***This is a trimed String**"
$trimmedString = $trimTarget.TrimEnd("*")
write-Host $trimmedString

$name = "Bob Ross"

# Problems to Solve...
# Make sure you understand how to list the methods and properties of string objects!
# -------------------------------------------------------------------- #
#1. Write the length of this string "abcdef" to the console
#    (Hint: Length)

#2. Create a new string that is composed of the number characters in the string "abc12345def" 
    # Hint: Substring -- Do Not use if,then,else or select
$targetString = "a2b3c51de4f"
$numberString = "12345"
$targetLength = $targetString.Length
$stringLength = $numberString.Length
# Go through each character in $targetString
for ($counter = 0; $counter -le $targetLength; $counter++) {
    #check to see if the current character is in $targetString
    if ($targetString.IndexOf($numberString($counter) -ne 0 {
        # if it is, add it to the result string
        $resultString = $resultString + $numberString[$counter]
    }
}
write-host The result string is $resultString

if ("def" -contains "ef") {
    write-host "def contains ef"
}

#3 Print out the reverse of this string   Abraham Lincoln  -> nlocniL maharbA
# Hints -- BEFORE you start, figure out an algorithm to do this
    # - Length of the string
    # - For Loop
    # - Substring

#4.  Replace all the forward slashes in "c:/users/rick/filename.docx" 
# with backslashes (\)

#5. Determine if this string is a legitimate Windows file name:
# (c:\user\jeff\filename)