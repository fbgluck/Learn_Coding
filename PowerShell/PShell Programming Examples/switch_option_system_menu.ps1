# switch_option 
<# 
Demonstrates how to use the switch option instead of alot of If.. Then... Else or if Elseif
#>
Clear-Host
#This is the if-elseif way to write a menu

write-host "****** System Menu With If elseif***********" -backgroundcolor red -foregroundcolor white
write-host
Write-host "1: Do task # 1 "
Write-host "2: Do task # 2"
Write-host "3: Do task # 3"
Write-host "q: Exit the program"
write-host "--------------------------------"
$userInput = Read-Host "Enter Your Selection >> " #Remember Read-Host always returns a string

if ($userInput -eq "1") {
    Write-Host "Now doing task Number 1"
}
elseif ($userInput -eq "2") {
    Write-host "Now doing task #2"
}
elseif ($userInput -eq "3") {
    Write-Host "Now doing task #3"
}
elseif ($userInput -eq "q") {
    write-host "Exiting the program... Bye"
}
else {
    Write-Host "Nothing was done because you can't follow directions!"
}

# ------------------------------------------------------------------------

write-host ""
write-host "****** System Menu with Switch ***********" -backgroundcolor red -foregroundcolor white
write-host
Write-host "1: Do task # 1 "
Write-host "2: Do task # 2"
Write-host "2: Do task # 2"
Write-host "q: Exit the program"
write-host "--------------------------------"
$userInput = Read-Host "Enter Your Selection >> " #Remember Read-Host always returns a string
switch ($userInput)
    {
        '1' {
            Write-Host 'Now Doing Task Number 1'
        }
        '2' {
            Write-Host 'Now Doing Task Number 2'
        }
        '3' {
            Write-Host 'Now doing Task Number 3'
        }
        'q' {
            Write-Host "Exiting The Program... Bye"
        }
        default {
            Write-host "Nothing was done because you can't follow directions!"
            write-host "It's time to say goodby"
        }
    }

    ## Question: How would you build a menu to run another script from this script?
