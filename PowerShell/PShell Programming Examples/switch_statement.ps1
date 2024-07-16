<# 
.DESCRIPTION
This program demonstrates the switch statement and how to build a menu
Concepts: Switch Statements
Concepts: Menus
Concepts: Break
#>

<#
SYNTAX:

Switch (<test-expression>) {
   <result1-to-be-matched> { <action> }
   <result2-to-be-matched> { <action> }
}
#>

$question = Read-Host "enter 1 or 7"
#7 options type one in while running
Switch ($question) {
   1 {Write-Host "you pick 1";Break}
   2 {Write-Host "you pick 2";Break}
   3 {Write-Host "you pick 3";Break}
   4 {Write-Host "you pick 4";Break}
   5 {Write-Host "you pick 5";Break}
   6 {Write-Host "you pick 6";Break}
   7 {Write-Host "you pick 7";Break}
   Default {Write-Host "Not correct"}
}  
#valid choice 
$question = Read-Host "choose true or false OR maybe"
Switch ($question) {
   True {Write-Host "you choose True";Break}
   False {Write-Host "you choose False";Break}
   Maybe {Write-Host "you choose Maybe";Break}
   Default {Write-Host "Not an option"}
}  



Clear-Host
Switch ($question) {
   1 {Write-Host "Multiply Two Numbers"
        $num1 = Read-Host "Enter The First Number"
        $num2 = Read-Host "Enter the Second Number"
         Write-Host "The Product is:" ($num1 * $num2)
       }
      }
       
       
    