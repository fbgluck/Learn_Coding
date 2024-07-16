#Number should be from 1-50
for ($counter = 1 ; $counter -le 10 ; $counter++)
 {  $num=get-random -Minimum 0 -Maximum 50
    if ($num -ge 25) {
    write-host $num "is High End"}
    else {write-host $num "low end"}
}   
