<# File Name: Disk_Free_Space.PS1
Author: Fredric Gluck
Date: 02/07/2020
Concepts: For-Each Object
Concepts: Working With The File System
Description: Returns the free space on each drive and the total free space in the system
#>

# ---------------------------------------------------------------------------------------------------
# Return a bunch of objects each of which represent a drive associated with the system.
# Pipeline them to the next operation. 
Get-PSDrive |
<# 
Filter the items returned so that we only see the objects
that have the property of Free greater than 1 and Pipeline it to the next Operation
#>

<# $_ is a special variable that represents the current object in the pipe #> 
where-Object {$_.Free -gt 1} |

<# From the objects returned, select only specific properties of the object to work with in this program #>
select-Object Name, Used, Free |

<# Now we are going to loop through each object and its returned properties and do something #>

<# ------------------------------- #>
<# ForEach-Object {
    write-host "Got One"
    } 
#>
 
<# ------------------------------- #>
<# The Lets write the amount of free space -- it will be written in bytes (yeeech) #>
<# ForEach-Object {
    write-host "Free Space for "$_.root "is" $_.Free -ForegroundColor yellow
    }
#>

<#--------------------------------- #>
<# Lets do the same thing but now we want to do math (use parenthesis) on the free space object using a built in PS capability #>
<#    ForEach-Object {
        write-host "Free Space for "$_.root "is" ($_.Free/1GB) -ForegroundColor Green
    }
#>
<# ------------------------------- #>

<#--------------------------------- #>
<# And lets do some formatting as a number with 2 decimal places to make it pretty.  #>

 <#   ForEach-Object {
        write-host "Free Space for "$_.root "is" ( "{0:N2}" -f ($_.Free/1GB) ) "GB" -ForegroundColor Green
    }
#>
<# ------------------------------- #>
<# Demonstrate How A Program Loop Works. 
    There are three parts - initialize, do and wrap up 
    This is a loop written with a lot of shortcuts.
#>
<#
ForEach-Object {$count=0; Write-Host "Beginning of the loop"}{Write-Host "The variable count is: "$count;$count = $count + 1}{write-host "All done!"} # or shortcut of $count++}
#>
<# ------------------------------------- #>
<# Here's an exploded way to write a loop so we understand it better #>
ForEach-Object -begin {
    $count = 0 ;
    $total_free = 0;
    Write-Host "---------------------------------------"
    Write-Host "Disk Usage On This System:";
    } -process {
        $_.Name + " -- Used: " + "{0:N2}" -f ($_.Used/1gb) + "gb" + " -- Free: " + "{0:N2}" -f ($_.Free/1gb) + "gb";
        $total_free = $total_free + $_.Free;
        $count = $count+1
    } -end {
        Write-Host "All Done. Examined "$count "drives";
        Write-Host "Total Free Space Available: "  ("{0:N2}" -f ($total_free/1gb)) "GB"-BackgroundColor Magenta
    }
    
 #>