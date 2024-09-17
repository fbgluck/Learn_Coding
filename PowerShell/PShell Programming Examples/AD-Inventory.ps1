# You need to install the AD Module first before you are allowed to 
# query the AD Controller
# Install the AD module as follows:
# 1. Go to this URL for a good article -- https://www.varonis.com/blog/powershell-active-directory-module
# 2. Install the option for Windows
# 3. Open PowerShell - Execute: Get-Module -Name ActiveDirectory - ListAvailable
# 4. Execute: Import-Module ActiveDirectory

Get-ADComputer -Filter "*"| format-table
# List all AD Computers on the Domain Sorted by Name
Get-ADComputer -Filter "*" | Select-Object Name |Sort-Object Name|Format-Table

# List all AD Computers on the domain Sorted by Name. Output to CSV file
Get-ADComputer -Filter "*" | Select-Object Name |Sort-Object Name| export-CSV c:\Users\fgluck\Downloads\ADInventory.csv

Write-Host "File Exported"

Write-Host "Re-import file"

# Now read the data from the file and process each line
$csvData = Import-Csv -Path "c:\Users\fgluck\Downloads\ADInventory.csv"
foreach ($line in $csvData) {  # Reads each line into an object called $line 
    # Process each line here
    Write-Host "Found Computer: ",$line.'Name'}

# Now get serious and process each line with something useful
Get-CimInstance -ClassName Win32_OperatingSystem |
  Select-Object -Property BuildNumber,BuildType,OSType,ServicePackMajorVersion,ServicePackMinorVersion, InstallDate | Format-Table