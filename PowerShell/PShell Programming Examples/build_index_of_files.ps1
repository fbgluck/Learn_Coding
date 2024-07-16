<# 
.SYNOPSIS
Open every file in the directory and produce an index and summary list
#>

# Preliminaries
Clear-Host # Clears screen
$verbosePreference = "Continue" # set option to continue after verbose message displayed (ref: PowerShell Preference Variables)
write-verbose -message "Program Starts at: $(get-date)" # How to display function along with message

# Declare and Initialize Variables
$fileCounter = 0 # loop counter
$target_directory = "." # Currently the current directory. Later let the user select

# Count the files in the current directory
$files = Get-ChildItem $target_directory
# print the variable type of $files so we can see what to do with it
Write-Verbose "Type of data returned is: $($files.GetType() )"
$totalNumberFiles = $files.count

# Start program by getting a list of file names in the directory
Get-ChildItem $target_directory |

# Iterate through the returned system.object list
ForEach-Object -begin {
        write-verbose "There are $($totalNumberFiles) files to be indexed. They are:" #count the number of items in the returned array
        Write-Host "(Starting array processing ....)"
        Write-Host "------------"

    } -process {  #iterate through the returned array
            $fileCounter++ #getting the next file so we increment the counter
            write-host "File" $fileCounter ": " ($_.Name -join "`n") #have to use this construct to get one item on each line
            # Allows us to read entire file and select lines that start with "." using REGEX
            $index_line = get-content $_.FullName | Where-Object {$_ -match "^[\.]"}
            write-host "Found: $index_line"
            write-host "------------"
        
    } -end {
        write-verbose "** Done **"
    }
