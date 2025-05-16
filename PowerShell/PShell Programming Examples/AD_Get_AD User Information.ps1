# Reads the AD Directory and 
# This does an inventory of users in AD
Clear-Host
# Get current date and time
$nowDate = Get-Date
Write-Host ("Program started at $($nowDate)")
# Use this command to find out all properties of a specific AD User
# Get-ADUser -Identity "fgluck" -Properties * | Select-Object *
# or for all uers
# Get-ADUser -Filter * -Properties * | Select-Object *
Get-ADUser -Filter * -Properties DisplayName, LastLogonDate |Sort-Object LastLogonDate |
    Select-Object @{Name="User Name";Expression={$PSItem.DisplayName}},
        @{Name="LastLogon";Expression={$PSItem.LastLogonDate}},
        @{Name="Days Since Last Login";
          Expression = { 
                $DaysSince = ((Get-Date)-$PSItem.LastLogonDate).Days
                    switch ($DaysSince) {
                        {($DaysSince) -ge 30}  {"$($PSStyle.Foreground.Red)$DaysSince $($PSStyle.Reset)"; break}
                        {($DaysSince) -lt 30}  {$DaysSince ; break}
                    } #End of Switch
                } # end of expression
            } # end of @name 
    | Format-Table -Autosize

Write-Host ("Finished...")
