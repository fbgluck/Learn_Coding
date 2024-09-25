<#
You need to install the AD Module first before you are allowed to 
query the AD Controller
Install the AD module as follows:
1. Go to this URL for a good article -- https://www.varonis.com/blog/powershell-active-directory-module
2. Install the option for Windows
3. Open PowerShell - Execute: Get-Module -Name ActiveDirectory - ListAvailable
4. Execute: Import-Module ActiveDirectory

This script produces a CSV file that can be opened with Excel
File Management -- 


Build the name of the output file to be used

1. Get user name to complete the output file name
I use the $env variable $env:USERPROFILE
(List all the env variables by the psCommand "dir env:")

2. The output file will be c:\<username>\Downloads\sysinv-<date>.csv

Get the date
#>
$fileDate = Get-Date -Format MM_dd_ssffff #ss = seconds ffff = miliseconds 4-digits
# Now build the file name
$fileName = $env:USERPROFILE + "\desktop\sysinv-" + $fileDate + ".csv"

# 1. Check if output file exists
if (Test-Path $fileName){
  # Delete the file if it does exist
  Remove-Item $fileName
  Write-Host "$fileName exist. Removing file"
}
# File does not exist - create the file and do not output the listing (default behavior)
New-Item -ItemType File -Path $filename |out-Null
write-Host "Output will be written to file:" $fileName

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
    Select-Object PSComputerName,ReleaseDate,Version | Export-CSV $fileName -Append
  } 
   else {
    # Write this message to the csv file
   "$target ,Did not respond to ping. System probably not online" | Out-File $fileName -Append
   }
}


