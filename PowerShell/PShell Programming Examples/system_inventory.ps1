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