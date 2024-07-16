<#
    Demonstrates how to check for a file, create a file then
    Write to a file. Code can be used at a template for writing logfiles
    output_write_txt_Log_file
    Uses SET-CONTENT to wrote content to a file (wipes out all previous content)
    Uses ADD-CONTENT to add content to the end of a file
    Uses TEST-PATH to test if a file exists
    Uses $env: Environment Variables
#>
#----------- Functions -------------- #

function write-logfile {
    # Formats and writes message to logfile with timestamp
    param ([string]$message)
    $LogMessage = "$NowTime>> $message"
    Add-Content -Path $FullLogFile -Value $LogMessage
}
# -------------------------------------------------- #
# First, test to see that the target folder exists and create if it doesn't
# We are using PS Env variables. To list them use: Get-Childitem -path env:
$HomeDrive = $env:HOMEDRIVE
# Note: PS does not understand drive letters (other than
#C:) so full pathnames Must be used!
# ------- File Name Variables --------------------
$HomeServer = "\\DC-07\Private_Drives\fgluck\"
$LogFileDIR = "\Logfiles"
$LogFileName = "\testlogfile.txt"
$CreateFilePath = $HomeServer + $LogFileDIR
$FullLogFile = $HomeDrive + $LogFileDIR + $LogFileName
$NowTime = Get-Date #Time Stamp for Log File
# ----------------------------------------------------
# Test to see if target file exists
Write-Host Full Pathname to LogFile is: $FullLogFile
if (Test-Path -Path $FullLogFile -PathType Leaf) {
    write-host $FullLogFile Exists... All is well
}
Else {                  # Target file does not exist so we create it
    write-host $FullLogFile Does Not Exist....Creating
    New-Item -Path $CreateFilePath -Name $LogFileName -ItemType "file" -Value "This is a text string."
    Write-Host "Folder Created successfully"
}
# Files have been checked. Now write contents to the file
Set-Content -Path $FullLogFile -Value "$NowTime>> Logfile started"
For ($counter = 1; $counter -le 10; $counter++) {
    write-logfile "Wrote line number $counter"
}
# Finish Up

<#
# Experimental section -- we should be able to email the logfile to me
$cred = Get-Credential  #Ask for userID and Password
Send-MailMessage `
-From 'fbgluck <fbgluck@gmail.com>' `
-To 'Fredric Gluck <fgluck@sanford.org>' `
-Subject 'Sending the Attachment' `
-Body "Forgot to send the attachment. Sending now." `
-Attachments $fullLogFile `
-Priority High `
-DeliveryNotificationOption OnSuccess, OnFailure `
-SmtpServer 'smtp.gmail.com' `
-Port 25 `
–UseTLS `
-Credential $cred
#>
write-host File $FullLogFile emailed
write-logfile $FullLogFile has been emailed

write-host File Written... Program Completed -BackgroundColor Red -ForegroundColor White