# A Snippit that gets information about the Notepad process on this computer
# Our goal is to eventually be able to look at and kill the process on our
# computer and on a remote computer.
get-process | #look at aliasproperty
where {$_.ProcessName -like "Note*"} |
select ProcessName, ID, StartTime, TotalProcessorTime, MachineName| 
Format-Table

