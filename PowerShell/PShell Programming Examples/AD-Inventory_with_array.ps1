# You need to install the AD Module first before you are allowed to 
# query the AD Controller
# Install the AD module as follows:
# 1. Go to this URL for a good article -- https://www.varonis.com/blog/powershell-active-directory-module
# 2. Install the option for Windows
# 3. Open PowerShell - Execute: Get-Module -Name ActiveDirectory - ListAvailable
# 4. Execute: Import-Module ActiveDirectory

#This is an empty array that will hold the names of the system
$machineNames = @()
# Fill the array with a list of retrieved names
$machineNames=(Get-ADComputer -Filter "*" | Select-Object Name |Sort-Object Name)
# 
Write-Host "There are: ",$machineNames.count," systems found."
Write-Host "    SysName        |                  Rel Date          |             BIOS Ver          "
Write-Host "----------------------------------------------------------------------------------------"
# Now iterate through the array and list each item
for ($i=0; $i -le $machineNames.count-1; $i=$i+1) {
  $target = $machineNames.Name[$i]
  # Test to see if the system in online by pinging it
  if (test-connection -TargetName $target -Quiet) # Returns true if ping successful
  {
    # Get the info from the system name in $target
    Get-CIMInstance -ClassName Win32_BIOS -ComputerName $target 
     # | Select-object PSComputerName, ReleaseDate, Version
     | Format-Table -HideTableHeaders -Property @{expression={$_.PSComputerName}; Label="Sys Name"; Width=20},
      @{expression={$_.ReleaseDate}; Label = "Rel. Date"; Width=40},
      @{expression={$_.Version}; Label="BIOS Ver."; Width=30}
  } 
   else {
    write-host $target, " did not respond to ping. System probably not online"
   }
}

# Output from this is horrible. Spaces between lines from Format-Table stinks.
# Could I create a custom object with the items I want to list and then
# Write-Host each of the properties on each line?
