# =======
# Get-ComputerInfo | Select-Object "BiosReleaseDate", "LogonServer", "CSModel"
Clear-Host
# Initialize Counting Variables
$enUsers = 0
$disUsers = 0
$totalMem=0 # Total Memory in System
$mbConverion = 1073741824 # Actual Number of Bytes in a Megabyte
$tempMem = 0
# Hash table for disk types detected by Get-CimInstance
# Ref: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-logicaldisk
$diskType = @{  }
    $diskType.add(0,"unknown")
    $diskType.add(1,"no root directory")
    $diskType.add(2,"Removable Disk")
    $diskType.add(3,"Local Disk")
    $diskType.add(4,"Network Drive")
    $diskType.add(5,"Compact Disk (CD)")
    $diskType.add(6,"RamDisk")

$PSStyle.Formatting.Underline = $true
Write-Host ("Local User Status for: $env:COMPUTERNAME") # contents of environment variable
$PSStyle.Formatting.Underline = $false
#Write-Host "----------------------------------"

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
Get-CimInstance -ClassName Win32_LogicalDisk |
# Select DeviceID, volumeName, Size, FreeSpace Status
Format-Table @{Label="DeviceID";Expression={$PSItem.DeviceID}},
    @{Label="VolumeName";Expression={$PSItem.VolumeName}},
    @{Label="DriveType" ;Expression = {
            switch ($PSItem.DriveType) { 
                0     {'unknown - (Type 0)'}
                1     {'No root directory (Type 1)'}
                2     {'Removable Disk (Type: 2)'}
                3     {'Local Disk (Type: 3)'}
                4     {'Network Drive (Type 4)'} 
                5     {'Compact Disk (Type 5)'}
                6     {'RAM Disk (Type 6)'}    
                default {"unavailable"}
            }  # End of switch
        } #End of Expression
    }, # End of Label
    @{Label="Size (GB)";Expression={$PSItem.Size/1073741824}},
    # @{Label="Free Space (GB)";Expression={$PSItem.FreeSpace/1073741824 }},
    @{Label="% Free ";Expression={($PSItem.FreeSpace/$PSItem.Size)*100}}

Write-Host "Display Adapters"
Write-Host "--------------------------------------"
# get-PnpDevice | Where-Object { $PSItem.Class -match 'Net|Display|Media' } |Select Status, Class,FriendlyName, Manufacturer | Sort-Object Class
# get-PnpDevice | Where-Object { $PSItem.Class -match 'Display' } | Select-Object Status,Manufacturer,FriendlyName

Get-WmiObject Win32_VideoController | Format-Table @{Label="Device";Expression={$PSItem.Name}},
    @{Label="AdapterRAM (GB)";Expression={$PSItem.AdapterRAM/1073741824}}


Write-Host "Physical Network Adapters"
Write-Host "--------------------------------------"

Get-NetAdapter -Physical |Select-Object Name, InterfaceDescription,LinkSpeed,NetworkAddresses,Status |Format-List
Get-NetIPAddress  |Select-Object IPv4Address, IPv6Address
