#arrays
# An array is a list of data items
# Arrays make it easier to reference items in a list
# https://ss64.com/ps/syntax-arrays.html

<# 
. FILE arays_overview.ps1
 .AUTHOR Fredric B. Gluck
 .DATE 04/04/2022
 .CLASS CNS 1
 .PURPOSE Demonstrate How Arrays Work
------------------------------------------------------------------------------------------

#>
Clear-Host
# Find methods and props of an array
# $a=1,2 
# $a | get-member # unary operator
# -------------------------------------------------------
$StartDate = Get-Date
Write-Host
Write-Host "Program Started at:" $StartDate.TimeOfDay -BackgroundColor red -ForegroundColor white

#Create some arrays
write-host "-------------------------------------"
Write-Host "Sample Array Information"
$sampleArray = @(1,2,3,4)
$sampleArray1 = "first",2,"third",3.21
write-host $sampleArray[0] # the first element is an array is [0]
write-host $sampleArray1[3] #proof that you don't have to have same types
$sumTest = $sampleArray1[3] + 99 #add two numbers
write-host $sumTest
write-host "-----------------------------------------"

# Two Arrays declared differently 
$nameArray = @("Frank", "Joe", "Jillian", "Hillary")
$hourlyRate = 12.00, 13.25, 21.20, 30.00, 12.34
write-host "NameArray is" $nameArray.length "elements long."
$nameArray += "Jackson" # Adding an element to the array at the end
$hourlyRate += 22.50
write-host "NameArray now has" $nameArray.Count "elements in it."
Write-Host "Hourly Rate now has" $hourlyRate.Count "elements in it"


write-host "-----------------------------------------"
# iterating through an array. Note the limit in the loop
# This is a loop that will work regardless of how many elements are in the array
For ($pointer=0;$pointer -le $nameArray.Count-1; $pointer++) {
    write-host "The name in array element $pointer is:" $nameArray[$pointer]
    write-host "Total Paycheck for" $nameArray[$pointer] "is: $"`
    ($hourlyRate[$pointer] * 40)  # assume 40 hour week
    write-host "-----------------------------------------------" 
}

# This code shows the end time and how much time the code took to run
$EndDate = Get-Date
Write-Host "Program Ended at: " $EndDate.TimeOfDay -BackgroundColor red -ForegroundColor white
Write-Host "Total Runtime: " ($EndDate.TimeOfDay - $StartDate.TimeOfDay) `r`n # return and  new line

#Parking Lot Questions:

# Yes, there are two dimensional Arrays

# Can you have an array that contains an array?

# How would you check to see if two arrays have the same number of elements
# and why would that be important in our salary calculation?