# Modifying Text Color and Style in Powershell using $PSStyle 
# Object which implements ANSI (Americain National Standards Institute)
# standards for character sequences that control the output of text
# on a terminal device.
#
# Lists all the object values in this variable
$PSStyle
# Example.... Note the use of Reset 
# Have to Reset after color is changed
# `e represents the ESC character
Write-Host "$($PSStyle.Foreground.Green)$($PSStyle.Background.Yellow)$($PSStyle.Underline)This is modified text.$($PSStyle.Reset)"
# ---------
Write-Host "This is normal text."
# -----
Write-Host "$($PSStyle.Reverse)This text is Reversed.$($PSStyle.Reset)"
# ----
Write-Host "This is $($PSStyle.Italic)italicized$($PSStyle.ItalicOff) text."
Write-Host "This is $($PSStyle.Blink)blinking$($PSStyle.BlinkOff) text. (Doesn't work)"
Write-Host "This is $($PSStyle.Strikethrough)strike through$($PSStyle.StrikethroughOff) text."