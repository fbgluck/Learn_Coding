# This gets the names of users in AD
Get-ADUser -filter "Surname -like '*'" | Select-Object Name

