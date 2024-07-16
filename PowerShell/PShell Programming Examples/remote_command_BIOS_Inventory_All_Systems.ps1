#BIOS_Inventory_All_Systems
<#
Notes: Invoke-Command requires that Win Remote Management
is enabled on all client computers. See these refs for
information about how to make this happen

You can test an individual system using the PS command (in admin mode):
test-wsman <IP address or computer name>

When using the CIM cmdlets to query remote devices, 
PowerShell uses WinRM, otherwise known as PowerShell
remoting. WinRM uses a secure connection and Active
Directory and Kerberos for authentication. 

ref: https://petri.com/how-to-inventory-remote-computers-using-powershell/


#>
# Get List of All Systems on Domain

# Initialize Array used to hold list of domain systems
$ADSystems=@()
Get-ADComputer -Filter * | 
    Select-Object Name |
    Sort-Object -Property Name |
     ForEach-Object {
        # Add computer name to array
        $ADSystems += $_.Name
        # ... and then remotely invoke the command
        <#
        For($counter =0; $counter -le $ADSystems.Length -1; $counter++) {
            Write-Host Querying $ADSystems[$counter]
            Add these back in when systems are configure for remote access
            Invoke-Command -ComputerName $ADSystems[$counter] -ScriptBlock { 
            get-CIMInstance -Class CIM_BIOSElement | Select-Object Manufacturer, Name, SerialNumber | Format-Table }  
            }
        #>
        }
        $LocalSystem = "DC-07"
        Write-Host Querying $LocalSystem
        Invoke-Command -ComputerName $LocalSystem -ScriptBlock { 
            get-CIMInstance -Class CIM_BIOSElement | Select-Object Manufacturer, Name, SerialNumber 
            | Format-Table }
        Invoke-Command -ComputerName $LocalSystem -ScriptBlock { 
            Get-CimInstance -Class win32_networkadapter | 
            Select-Object -Property SystemName, Manufacturer, ProductName, MACAddress, Speed |
            Where-Object -FilterScript {$_.MACAddress -NE $null}
        }


