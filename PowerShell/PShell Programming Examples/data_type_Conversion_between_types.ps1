# Conversion from one data type to another and demonstration of try and catch
$UserInput = read-host -Prompt "Please enter an integer" #Read-Host always assumes a string
try {
    $mutiplier = [int]$UserInput #convert from str to int. If an error occurs, catch will be executed
}
catch {
    #This code is executed if the code in try throws an error
    Write-Host "Sorry, you should have entered an integer"
}
#build the multiplication table
Write-host "----------------------"
for ($counter = 1; $counter -gt 50; $counter++) {
    $answer = ($counter * $mutiplier)
    Write-host "$counter * $multiplier = $answer"
}