<<<<<<< HEAD
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


=======
# Get-ComputerInfo | Select-Object "BiosReleaseDate", "LogonServer", "CSModel"
Clear-Host
# Initialize Counting Variables
$enUsers = 0
$disUsers = 0
Write-Host ("Local User Status for: $env:COMPUTERNAME") # contents of environment variable
Write-Host "----------------------------------"

Get-LocalUser | 
ForEach-Object -Process {
    write-host ("Local user: $($PSItem.Name)") -NoNewline # For the current item in the for each
    if ($PSItem.Enabled) {      #.Enabled is a boolean value
        write-host (" is Enabled") -ForegroundColor "Red"
        $enUsers=$enUsers+1
    }
    else {
        write-host (" is Disabled") -ForegroundColor "Green"
        $disUsers = $disUsers +1
    }
} # end of Process Loop
Write-Host "--------------------------------------"
Write-Host ("Total of $enUsers enabled users")
Write-Host ("Total of $disUsers disabled users")
Write-Host

$cpuInfo = Get-CimInstance -ClassName Win32_Processor
write-Host$cpuInfo.Name -contains "Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz" # should be True
>>>>>>> d3512ce7fb3c8d7c0db5c07e284cd682a30e44a2
