Get-Process | 
    Select-Object Name, CPU, 
    @{label='Status';expression={
        if ($_.CPU -gt 100) {'High'} 
        elseif ($_.CPU -gt 50) {'Medium'} 
        else {'Low'}}}