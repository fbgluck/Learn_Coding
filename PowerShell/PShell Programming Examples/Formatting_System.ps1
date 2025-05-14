<#
# Formatting System - These are the cmdlets that allow you to
format output in various formats. If they are not used,
PSH makes its own decision about how the format to the console
is going to look.

try: help format
#>

# Format-Wide
# Format-List
# Format-Table
# Format-Custom
Clear-Host
Get-Service 
    |where-Object -property {$PSItem.status -EQ "stopped"}
    |Format-Table Name, Status, CanShutdown 
    |more
Get-Service | Where-Object { $_.Status -eq "Stopped" }

#Get-Service | Format-List Name, Status, CanShutdown
#Get-Service | Format-Wide  -Column 3
#Get-Service | Format-Custom Name, Status, CanShutdown