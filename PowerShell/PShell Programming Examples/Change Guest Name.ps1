<#
.FILE_NAME 
Change Guest Name.ps1

.AUTHOR 
Fredric Gluck

.DATE
2/10/2021

.SYNOPSIS
This script illustrates If Else statement and changes the Full Name of a local user

.INDEX
Interate through Object
If Then Else
User Information

.KEYWORDS
Object
Conditonal

#>

#----------------------------------------------------------------------------------#
# Get-LocalUser | Get-Member

# Retrieve All The Local Users On The System
Get-LocalUser|
# Grab three properties for the collection
Select-Object Name, FullName, LastLogin |
#Now go through each Object in the collection
ForEach-Object -begin {
    write-host "Processing All Users";
  } -process {
    If ($_.Name -eq "Guest") {
        write-host "Yep... It's" $_.Name
        set-LocalUser -Name Guest -FullName "THE X GUEST"
        write-host "I've Changed the Full Name"
    } Else {
        (write-host "Nope, not guest. It's " $_.Name)
    }

  } -End {
   Write-Host "Processed All Users. Listing Results"
  } # End of -End
#
# Now Let's List the Results
Get-LocalUser | Select-Object Name, FullName, LastLogin, Enabled
#>