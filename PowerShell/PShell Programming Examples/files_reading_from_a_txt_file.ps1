<#

files_reading_from_a_file

.DESCRIPTION: Reads each line from a .txt file, modifies the line and writes it
to the console.

.REFERENCE: https://www.delftstack.com/howto/powershell/read-files-line-by-line-in-windows-powershell/
 
Note: The Get-Content CMDLET reads an entire file into memory as it creates
 an object. This may cause issues if the files are large. We use a loop to read
 one line at a time.
#>
# ------- File Name Variables --------------------
$HomeServer = "\\DC-07\Private_Drives\fgluck\"
$LogFileDIR = "\Logfiles"
$LogFileName = "\testlogfile.txt"
$FullLogFile = $HomeDrive + $LogFileDIR + $LogFileName
$NowTime = Get-Date #Time Stamp for Log File
# ----------------------------------------------------
# Test to see if target file exists
Write-Host Full Pathname to LogFile is: $FullLogFile
if (Test-Path -Path $FullLogFile -PathType Leaf) {
    write-host $FullLogFile Exists... All is well.. Reading File
    $fileExists = $true
}
Else {
    # Target file does not exist so we create it
    write-host $FullLogFile Does Not Exist.... Program terminating
    $fileExists = $false
}
# Files have been checked. Now read contents from the file
# 

If ($fileExists) {
    ForEach($fileLine in Get-Content $FullLogFile) {  #each line of the file
        Write-Progress -PercentComplete
    $changedLine = "$NowTime" + " " + "ALTERED: " +$fileLine
    # We write each file to the host but you probably want to do something
    # A bit more exciting (e.g. read the line into an array or use REGEX to
    # check formats )
    write-host $changedLine # Boring but it gets the point across
    }
}
write-host Done...