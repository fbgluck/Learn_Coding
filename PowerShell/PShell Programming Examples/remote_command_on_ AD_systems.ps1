<#
Originally by Evan Lowery (CNS1 - 2021)

NOTE: Prior to running the Get-ADComputer cmdlet, you must install RSAT Active Directory Domain Services
and Lightweight Directory Service tools. This is an installable feature. Go to SETTINGS > 
Optional Features >Add A Feature and select this feature to install. 
(ref: https://www.microsoft.com/en-us/download/details.aspx?id=45520)


Also - run the command "winrm quickconfig" on a workstationto check the status of the WinRM service which must 
be running on the target machine for it to be allowed to respond to remote Commands. WinRM Service
can be configured to be started and to be set in Delayed AutoStart mode.

More Also - the firewall needs to be configured properly to allow these requests into a system
#>
# Preliminaries
Clear-Host # Clears screen
$verbosePreference = "Continue" # set option to continue after verbose message displayed (ref: PowerShell Preference Variables)
write-verbose -message "Program Starts at: $(get-date)" # How to display function along with message
Get-NetConnectionProfile
# break
# Start by getting a list of all computers in the domain
Get-ADComputer -filter * | ForEach-Object -begin {
    write-host " Starting scan " -ForegroundColor White -BackgroundColor Blue
    } -process { write-verbose "Trying $_.Name..."
    # invoke the PS command on each computer
    invoke-command -computername $_.Name -command {
        Get-WMIObject Win32_ComputerSystem | select-object Manufacturer, Model
        $bios = Get-WMIObject win32_bios -Property ReleaseDate
        $bios.ConvertToDateTime($bios.ReleaseDate) | select-object DateTime
    }
    } -end {
        write-verbose "** Done **"
    }
