# ref: https://quizlet.com/382672871/powershell-flash-cards/

# First get all items in the Security EventLog
Get-EventLog -LogName Security |
# Then, from the object returned, select the last 5 and the items indicated
# Last 5 was the only way I could find to get the last 5 items in the log since
# there is no -Oldest parameter for the Get-EventLog
Select-Object -last 5 index,timeGenerated,source,message |
# And sort them by
Sort-Object  Index, TimeGenerated |
# And do some fancy formatting into a table
Format-Table -AutoSize -Wrap |
Out-File C:\Users\fgluck\Desktop\securityLog.txt
