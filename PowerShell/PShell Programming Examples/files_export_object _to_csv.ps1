# File_Output
# Export an Object to a CSV file
# Help Export-Csv
# Make sure you are in Home directory
Set-Location $Home
$targetPath = "./PSOutput/bios_output.txt"
# Check to see if file exists
if (Test-Path -Path $targetPath){
# Delete the existing file
    Write-Host ("File - $($targetPath) exists.")
    Write-Host ("Deleting File $($targetPath)")
    Remove-Item $targetPath
}
Write-Host (">> Writing output to: $($targetPath)")
# Grab the information and export each property to a CSV file
# Which can later be imported into Excel for further processing
Get-CimInstance -ClassName CIM_PhysicalMemory | 
    Select-Object -Property Tag, DeviceLocator, Capacity|
    Sort-Object Tag|
    Export-CSV $targetPath

Write-Host ("Completed... output written to $($targetPath)")
