# This program classifies 10 random numbers into two categories


Write-Host "Program Starting..."    
For ($counter = 1; $counter -le 10; $counter++) 
    {
    # Generate a random number between 1 and 50
    $randomNumber = get-random -minimum 0 -maximum 50
    # The NoNewLine parameter makes sure that a RETURN is not printed 
    Write-Host "Round " $counter ": The Number" $randomNumber "is " -NoNewline
    # Classisfy the Number based on its value
    if ($randomNumber -ge 25) {
        write-host "High End" 
    }
    else {
        write-host "Low End"
    }
}