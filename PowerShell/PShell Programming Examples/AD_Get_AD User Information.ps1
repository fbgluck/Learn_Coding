# Reads the AD Directory and 
# This does an inventory of users in AD
Clear-Host
# Get current date and time
$nowDate = Get-Date
Write-Host ("Program started at $($nowDate)")
Get-ADUser -Filter * -Properties LastLogonTimeStamp |
     Format-Table 
        @{
            Label="User Name";
            Expression={$PSItem.Name}
        },

        @{
            Label="Last Login";
            Expression={$PSItem.LastLogonTimestamp}
        },
        @{
            Label="Days Elapsed";
            Expression= {($nowDate - $PSItem.LastLogonTimeStamp).TotalDays}
        },
        @{
            Label="Time Since Last Login";
            Expression={
                $elapsedTime = $nowDate - $PSItem.LastLogonTimeStamp.Days
                if ($elapsedTime -ge 30) {
                    "$elapsedTime *"
                } else {
                    "$elapsedTime"
                }
            } #End of expression
        }
#>
Write-Host ("Finished...")
