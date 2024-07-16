get-wmiobject -class win32_quickfixengineering | # Get-Members
sort HotFixID -descending |
select HotFixID, Description, InstalledOn, Caption |
Format-Table
