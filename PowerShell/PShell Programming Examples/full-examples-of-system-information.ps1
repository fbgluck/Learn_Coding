# These are the commands lists in the PS Tutorial from Learn Microsoft
# https://learn.microsoft.com/en-us/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.4

Clear-Host
#
Write-Host "** CIM Demonstration Code **"
Write-Host "--------------------------------------"

Write-Host "** Return Information about current desktops in use **"
Get-CimInstance -ClassName Win32_Desktop
Write-Host "--------------------------------------"

Write-Host "** Return Information about current desktops  and exclude certain properties **"
Get-CimInstance -ClassName Win32_Desktop | Select-Object -ExcludeProperty "CIM*"
Write-Host "--------------------------------------"

Write-Host "** Retrieve Information about the System BIOS on a specific computer **"
# Get-CimInstance -ClassName Win32_BIOS -ComputerName ITN-DESKTOP-01
Write-Host "--------------------------------------"

Write-Host "** Get and list Processor Information on this computer **"
Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*"
Write-Host "--------------------------------------"

Write-Host "** Get specific information regarding System Type of this computer **"
Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property SystemType
Write-Host "--------------------------------------"

Write-Host "** Get system information and model **"
Get-CimInstance -ClassName Win32_ComputerSystem
Write-Host "--------------------------------------"

Write-Host "** List Installed Hot Fixes **"
Get-CimInstance -ClassName Win32_QuickFixEngineering
Write-Host "--------------------------------------"

Write-Host "List specific ID of Hot Fix **"
Get-CimInstance -ClassName Win32_QuickFixEngineering -Property HotFixID
Write-Host "--------------------------------------"

Write-Host "** Select Specific Information (HotfixID) of installed HotFixes"
Get-CimInstance -ClassName Win32_QuickFixEngineering -Property HotFixId |
    Select-Object -Property HotFixId
Write-Host "--------------------------------------"

Write-Host "** Get specific OS-Information **"
Get-CimInstance -ClassName Win32_OperatingSystem |
  Select-Object -Property BuildNumber,BuildType,OSType,ServicePackMajorVersion,ServicePackMinorVersion
Write-Host "--------------------------------------"

Write-Host "** Get All OS Information **"
  Get-CimInstance -ClassName Win32_OperatingSystem 
  Write-Host "--------------------------------------" 

Write-Host "List Local Users and Owners"
Get-CimInstance -ClassName Win32_OperatingSystem |
    Select-Object -Property NumberOfLicensedUsers, NumberOfUsers, RegisteredUser
Write-Host "--------------------------------------"

Write-Host "Show available Disk Space for Hard Drives (Type=3)"
Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3"
Write-Host "--------------------------------------"

Write-Host "Specific Information - Show available Disk Space with Total by category"
Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3" |
    Measure-Object -Property FreeSpace,Size -Sum |
    Select-Object -Property Property,Sum
Write-Host "--------------------------------------"

Write-Host "Get Login Session Information"
Get-CimInstance -ClassName Win32_LogonSession
Write-Host "--------------------------------------"

Write-Host "Get User Logged In To Current Session"
Get-CimInstance -ClassName Win32_ComputerSystem -Property UserName
Write-Host "--------------------------------------"

Write-Host "Get Local Time From Computer"
Get-CimInstance -ClassName Win32_LocalTime
Write-Host "--------------------------------------"

Write-Host "Get Service Informaton from Local Computer"
Get-CimInstance -ClassName Win32_Service |
    Select-Object -Property Status,Name,DisplayName
Write-Host "--------------------------------------"

Write-Host "Service Information In A Nice Format"
Get-CimInstance -ClassName Win32_Service |
    Format-Table -Property Status, Name, DisplayName -AutoSize -Wrap
Write-Host "--------------------------------------"

Write-Host "Basic OS Version Information for a specific computer in a table"    
Get-CimInstance -ClassName Win32_OperatingSystem  -ComputerName ITN-INSTRUCTOR|
    Format-Table -Property PSComputerName, InstallDate, Version,BuildNumber