<# 
. FILE for_loop_demonstration.ps1
 .AUTHOR Fredric B. Gluck
 .DATE 03/28/2022
 .CLASS CNS 1
 .PURPOSE Use a For Loop to create multiplication tables
------------------------------------------------------------------------------------------

#>
Clear-Host
$StartDate = Get-Date
Write-Host
Write-Host "Program Started at:" $StartDate.TimeOfDay -BackgroundColor red -ForegroundColor white
 <# Code Goes Here#>
# This code shows the end time and how much time the code took to run
$EndDate = Get-Date
Write-Host "Program Ended at: " $EndDate.TimeOfDay -BackgroundColor red -ForegroundColor white
Write-Host "Total Runtime: " ($EndDate.TimeOfDay - $StartDate.TimeOfDay)