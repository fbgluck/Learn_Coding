# =======
# Get-ComputerInfo | Select-Object "BiosReleaseDate", "LogonServer", "CSModel"
Clear-Host
# Initialize Counting Variables
$enUsers = 0
$disUsers = 0
$totalMem=0 # Total Memory in System
$mbConverion = 1073741824 # Actual Number of Bytes in a Megabyte
$tempMem = 0
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
Write-Host "--------------------------------------"

## CPU Information 
Write-Host
Write-Host("CPU Information")
Write-Host "--------------------------------------"
Get-CimInstance -ClassName Win32_Processor | ForEach-Object -Process {
    Write-Host ("$($PSItem.DeviceID) -- ") -NoNewline
    Write-Host ($PSItem.Name) -NoNewline
    Write-Host (" // $($PSItem.NumberOfCores) cores")
}
Write-Host "--------------------------------------"
## Memory Information
Write-Host
Write-Host("Memory Information")
Write-Host "--------------------------------------"
Get-CimInstance -ClassName CIM_PhysicalMemory | ForEach-Object -Process {
    Write-Host ("$($PSItem.Tag):  ")
    Write-Host ("    Slot: $($PSItem.DeviceLocator)")
    Write-Host ("    Part No: $($PSItem.PartNumber)")
    Write-Host ("    Speed: $($PSItem.Speed)Mhz")
    $tempMem = $PSItem.Capacity/1073741824 
    Write-Host ("    Capacity: $($tempMem)GB")
    $totalMem = $totalMem + $tempMem
}
Write-Host
Write-Host ("Total System Memory: $totalMem GB") -ForegroundColor Yellow
Write-Host "--------------------------------------"
## Storage

Write-Host
Write-Host("Storage")
Write-Host "--------------------------------------"
