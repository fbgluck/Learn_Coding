<# -- Multiline comment
.SYNOPSIS
Examine every item in the directory and produce an index and summary list
#>
# Preliminaries

Clear-Host # Clears screen

# set option to continue after verbose message displayed (ref: PowerShell Preference Variables)
$verbosePreference = "Inquire"  # Pause and ask the user how to continue
write-verbose -message "Program Starts at: $(get-date)" # How to display function along with message

# Declare and Initialize Variables
$fileCounter = 0 # loop counter
$target_directory = $Home #Currently the home directory. Later let the user select

# Count the files in the current directory
$files = Get-ChildItem $target_directory
# print the variable type of $files so we can see what to do with it
Write-Verbose "Type of data returned is: $($files.GetType() )"
$totalNumberFiles = $files.count
# Start program by getting a list of file names in the directory
# Note the use of -Begin, -Process and -End. These have to be positioned like this
# or syntax / processing errors will occur
Get-ChildItem $target_directory | ForEach-Object -Begin {
    Write-Host 
    Write-Host "There are $($totalNumberFiles) items in this folder. They are:" #count the number of items in the returned array
    # Write-Host "(Starting array processing ....)"
    Write-Host "------------"
    
    #iterate through the returned array
    }-Process {  
        $fileCounter++ #getting the next file so we increment the counter
        if ($PSItem.mode -like "d*"){
            Write-Host ("Item $($fileCounter): $($PSItem.Name) is a Directory") 
        }
        else {    
            # Allows us to read entire file and select lines that start with "." using REGEX
            # write-verbose ("In Else with $($PSItem.Name)")
            Write-Host ("Item $($fileCounter): $($PSItem.Name) is a File")                                    #$index_line = get-content $_.FullName | Where-Object {$_ -match "^[\.]"}
            #write-host "Found: $index_line"
        }
        
    }-end {
        write-host "------------"
        Write-Host ("Directory: $($target_directory.Name)")
        write-Host "** Done **"
} ## End of For-EachObject

