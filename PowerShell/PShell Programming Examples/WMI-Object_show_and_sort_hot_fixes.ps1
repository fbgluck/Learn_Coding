# This program illustrates how to use get-wmiobject to show hot fixes installed
# Concepts: WMIObject
# Concepts: Getting Selecting and Sorting Obhects
# Concepts: Formatting Output with Format-Table
# Concepts: Pipeline
get-wmiobject -class win32_quickfixengineering | # Get-Members
sort HotFixID -descending | # Sort results
select HotFixID, Description, InstalledOn, Caption |  # List Information
Format-Table
