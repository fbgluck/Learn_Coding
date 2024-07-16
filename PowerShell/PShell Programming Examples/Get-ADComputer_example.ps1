<#
This program gets information from the AD and is intended
to provide a quick overview of important AD contents
 Checklist
 1) Figure out what is meant by "Inventory". What information do I need?
 2) Figure out how to get one piece of this information on my local computer
 3) Expand the capability and get all inventory from my local computer
 4) Figure out how to get a list of all computers in my domain
 5) Figure out to get one piece of inventory information on one remote computer
 6) Expand the capability to get all inventory from a single remote computer
 7) Figure out how to get all inventory from all computers on the domain
 8) Celebrate!!
#>

# Example of GetADComputer use for Inventory
Write-Host "Domain Computers" -BackgroundColor Yellow -ForegroundColor Black
Get-ADComputer -Filter "name -like '*'" -Properties Name, LastLogonDate, IPv4Address, OperatingSystem 
| Sort-Object -property Name #Sort needs to come before Format-table
| Format-Table Name, LastLogonDate, IPv4Address, OperatingSystem -AutoSize 
#  
# Domain User Inventory
Write-Host "Domain Users" -BackgroundColor Yellow -ForegroundColor Black
Get-ADUser -Filter "name -like '*'" -properties Surname, GivenName, SamAccountName
| sort-Object Surname
| Format-Table Surname, GivenName, SamAccountName -AutoSize


# Inactive System List
$DaysInactive = 10
# $time variable converts $DaysInactive to LastLogonTimeStamp 
# property format for the -Filter switch to work
$time = (Get-Date).Adddays( - ($DaysInactive))
Write-Host "Inactive Systems for $daysInactive Days (Since $time)" -BackgroundColor Yellow -ForegroundColor Black
# Identify inactive computer accounts
Get-ADComputer -Filter { LastLogonTimeStamp -lt $time } -Properties Name, OperatingSystem, SamAccountName, DistinguishedName, LastLogonDate
| sort-Object LastLogonDate, Name
| Format-Table Name, LastLogonDate, OperatingSystem -AutoSize