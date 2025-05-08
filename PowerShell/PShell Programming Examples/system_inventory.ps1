Clear-Host # Clear Screen When We Start
# EXAMPLE: Use the cmdlet Get-ComputerInfo to get properties of this computer
# Get-ComputerInfo | Select-Object "CSName","CSDomain","BiosReleaseDate", "LogonServer", "CSModel"

# Assign the returned object to a single variable (of type object)
$OSInfo = Get-ComputerInfo
# Access a specific property of the object from the object variable
# $() is string interpolation in PShell
# Build full computer name
Write-Host "Full Computer Name is: $($OSInfo.CsName).$($OsInfo.CSDomain)"
# Check to see if it is the Instructor workstation
if ($($OSInfo.CSName) -eq "ITN-INSTRUCTOR") {
    write-host "  >> This is the instructor workstation **"}
    else {write-host $num "This is just a regular workstation"}
# Display another property of the object
Write-Host "Windows Product ID is: $($OSInfo.WindowsProductId)"
Write-Host " ------------------------------ "

# Process another set of information
Write-Host "The Following Local Users Are On This System:"
$localUsers = Get-LocalUser
$localUsers.Enabled
write-host ($localUsers.Enabled)
# Interate through an object 
foreach ($name in $localUsers.Name) 
{
    if ($localUsers.Enabled) {
    # check to see if acount is enabled
        write-Host (" >> Local User: $($name) is enabled")
    } else {
        write-Host (" >> Local User: $($name) is disabled")
    }
}


