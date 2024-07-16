Clear-Host
# Execute script from script
# Use the Powershell Invocation operator (&) to execute the script
# get-location
$psFileName= "\Hello_World_Extended.ps1" #the file name that will be run
# build the complete file name
$scriptLocation = "G:\My Drive\Class Curriculum Material\CNS 1 (Information Technology)"
$scriptLocation = $scriptlocation + "\@Introduction to Programming\PowerShell\Programming Examples"
$fullPathName = $scriptLocation + $psFileName
# Now that we have the complete file name, you can execute
write-host "Executing $fullPathName" -BackgroundColor red -ForegroundColor white
& $fullPathName # Execute the script using the Powershell Invocation Operator
Write-Host "Program $psfilename Completed..." - -backgroundcolor red -ForegroundColor white