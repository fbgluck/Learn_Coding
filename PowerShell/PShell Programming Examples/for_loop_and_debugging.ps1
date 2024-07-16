<# 
. FILE for_loop_demonstration.ps1
 .AUTHOR Fredric B. Gluck
 .DATE 03/28/2022
 .CLASS CNS 1
 .PURPOSE Show the construction and purpose of a for loop
------------------------------------------------------------------------------------------

#>
Clear-Host
$StartDate = Get-Date
Write-Host
Write-Host "Program Started at:" $StartDate.TimeOfDay -BackgroundColor red -ForegroundColor white
# This is an example of a for loop. It prints the values between 1 and 25
for ($counter = 1; $counter -le 25; $counter++) {
    write-host "The value of counter is: $counter "
} 
# This code shows the end time and how much time the code took to run
$EndDate = Get-Date
Write-Host "Program Ended at: " $EndDate.TimeOfDay -BackgroundColor red -ForegroundColor white
Write-Host "Total Runtime: " ($EndDate.TimeOfDay - $StartDate.TimeOfDay)