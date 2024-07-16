<#  
      .SYNOPSIS  
           Retrieve Manufacture Date from BIOS (local and remote systems)  
        
      .DESCRIPTION  
           This script is deployed out to machines so the manufacture and ownership dates are populated as a WMI entry. This allows for easy query of this information for depreciation and lifecycle purposes.  
        
      .NOTES  
           ===========================================================================  
           Created with:     Powershell ISE  
           Created on:       03/04/2021 8:55AM 
           Created by:       Fredric Gluck  
           Filename:         Lab30_Remote_PowerShell.ps1  
           ===========================================================================  
           The remote system will need to have the WIN-RM service running. This can be
           started by the PS command "Enable-PSRemoting"

      .REFERENCES
        https://mickitblog.blogspot.com/2019/12/wmi-query-for-dell-manufacture-and.html
        https://www.howtogeek.com/117192/how-to-run-powershell-commands-on-remote-computers/
        https://sid-500.com/2019/07/30/powershell-retrieve-list-of-domain-computers-by-operating-system/
 #> 
 $computer_name = "CNS-880W4L2"
 # $computer_name = "Instructor-D212"
 # $computer_name = "DC-07"
 # $computer_name = "CNS-DESKTOP-2"
 write-host "The computer you are going to query is: " $computer_name

<#
 Invoke-Command -ComputerName $computer_name {
  Get-WmiObject -Class Win32_BIOS |
 Select __SERVER, Manufacturer, SerialNumber, ReleaseDate, SystemBIOSMajorVersion, SystemBiosMinorVersion, Version, BuildNumber, Caption  

 }
 #>

 Get-WmiObject -Class Win32_BIOS  -ComputerName $computer_name|
 Select __SERVER, Manufacturer, SerialNumber, ReleaseDate, SystemBIOSMajorVersion, SystemBiosMinorVersion, Version, BuildNumber, Caption
 # Get the Architecture of the System
 # (Get-CimInstance CIM_OperatingSystem).OSArchitecture
 # Get Information about the processor
 Get-WmiObject Win32_Processor  -ComputerName $computer_name|
 Select PSComputerName, Name, AddressWidth
 write-host "---------------"
 Get-WmiObject win32_SystemEnclosure -Computer $computer_name
 
 <#
 That's most likely an issues on the remote PC.
- Doublecheck you have the right machine name
- Check if the machine is on and has network connection
- Check firewall ( "Windows Management Instrumentation (WMI-In)" rule )
- Check if WMI and it's dependencies are running
( Remote Access Auto Connection Manager Remote Access Connection Manager Remote Procedure Call (RPC) Remote Procedure Call (RPC) Locator Remote Registry)
- Check if DCOM is enabled (  Key: HKLM\Software\Microsoft\OLE, value: EnableDCOM [should be 'Y'])
 #>
 
  