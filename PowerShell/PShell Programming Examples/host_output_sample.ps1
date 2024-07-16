# Description: This code shows various options to write to Host
# Concepts: Host Output
# Concepts: Error Messages
Write-Error "431A: No intelligence" -Category "InvalidResult"
Write-Host "Write-Host writes to the console"
# How to write a progress bar
For ($count=1;$count -le 100; $count++)
    {
    Write-progress -Activity "Loop In Progress" -Status "$count% complete:" -PercentComplete $count;
    Start-Sleep -milliseconds 100;
    }
Write-Host  #blank line
Write-Warning -Message "This is a warning message written with write-warning"