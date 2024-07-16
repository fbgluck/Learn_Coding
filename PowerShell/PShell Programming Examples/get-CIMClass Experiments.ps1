# This is a scratchpad to explore Get-CIM functions
Clear-Host

Get-CimClass|Sort-Object -Descending

# Get-CimInstance -ClassName Win32_Fan
# Get-CimInstance -ClassName CIM_VoltageSensor
# Get-CimInstance -ClassName CIM_Memory


#Get-WmiObject -Class Win32_NetworkAdapter | get-member
#Get-WMIObject -Class Win32_NetworkAdapter | Select-Object "*"
#Get-WMIObject -Class Win32_NetworkAdapter | Select-Object -Property SystemName, Manufacturer, ProductName, MACAddress, Speed
function sectionDivider {
    param ([string] $topic)
    Write-Host ""
    Write-Host "** ---------- $topic ---------- **" -BackgroundColor Yellow -ForegroundColor Black
}

sectionDivider "System Hardware Report"

sectionDivider "BIOS Information"
get-CIMInstance -Class CIM_BIOSElement |Select-Object Manufacturer, Name, SerialNumber | Format-Table

sectionDivider "Network Adapter" 

# An Analysis of the network adapter on this sytem
Get-CimInstance -Class win32_networkadapter | 
    Select-Object -Property SystemName, Manufacturer, ProductName, MACAddress, Speed |
    Where-Object -FilterScript {$_.Speed -NE $null}

sectionDivider "Disk Storage" 
# Get-CIMInstance  -class Win32_DiskDrive | get-member 
Get-CIMInstance -ClassName Win32_DiskDrive |
    Select-Object -Property Name, Model, Size, Partitions

sectionDivider "Memory"
Get-CIMInstance -ClassName Win32_PhysicalMemory |
    Select-Object -Property Manufacturer, PartNumber, Capacity, Speed, SerialNumber

sectionDivider "Processor"
# This will not output correctly if it is the first item listed ?? Asynchronous ?? Synchronous -- more research needed!
Get-CIMInstance -ClassName Win32_Processor |
Select-Object -Property Name, MaxClockSpeed, CurrentClockSpeed 

sectionDivider "Keyboard"
Get-CimInstance -ClassName CIM_Keyboard |
Select-Object -Property Name, NumberOfFunctionKeys

sectionDivider "General OS Info"
Get-ComputerInfo |
    select-object -Property WindowsProductName, OsBuildNumber, OsHotFixes

