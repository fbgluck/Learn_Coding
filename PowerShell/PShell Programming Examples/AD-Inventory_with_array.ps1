# You need to install the AD Module first before you are allowed to 
# query the AD Controller
# Install the AD module as follows:
# 1. Go to this URL for a good article -- https://www.varonis.com/blog/powershell-active-directory-module
# 2. Install the option for Windows
# 3. Open PowerShell - Execute: Get-Module -Name ActiveDirectory - ListAvailable
# 4. Execute: Import-Module ActiveDirectory

# This script produces a CSV file that can be opened with Excel
# File Management -- 
# Build the name of the output file to be used
#1. Get user name to complete the output file name
#2. The output file will be c:\<username>\Downloads\sysinv-<date>.csv

#1. Check if output file exists
#2. If so, delete the file
#3. Create the new file
#4. Make sure you APPEND output to that file

# -----------  Obtain and Process Systems
#This is an empty array that will hold the names of the system
$machineNames = @()
# Fill the array with a list of retrieved names
$machineNames=(Get-ADComputer -Filter "*" | Select-Object Name |Sort-Object Name)
# Header for the output
Write-Host "There are: ",$machineNames.count," systems found."

# Now iterate through the array and list each item
# Array index starts at 0
for ($i=0; $i -le $machineNames.count-1; $i=$i+1) {
  $target = $machineNames.Name[$i]
  Write-Host "Processing System  $i - $target..."
  # Test to see if the system in online by pinging it
  if (test-connection -TargetName $target -Quiet) # Returns true if ping successful
  {

     ### Output to CSV (because later on, we can ope with Excel) ###
    Get-CimInstance -ClassName Win32_Bios -ComputerName $target |
    Select-Object PSComputerName,ReleaseDate,Version | Export-CSV c:\Users\fgluck\Desktop\bios_Report.csv -Append
  } 
   else {
    # Write this message to the csv file
   "$target did not respond to ping. System probably not online" | Out-File c:\Users\fgluck\Desktop\bios_Report.csv -Append
   }
}


