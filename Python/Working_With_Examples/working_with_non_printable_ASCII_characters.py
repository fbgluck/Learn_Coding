# Working With Non Printable ASCII Characters
# Ref: https://www.rapidtables.com/code/text/ascii-table.html
# Refer to a ASCII for the hex values of the characters
# we are printing
# This method is often used to output characters that can not be typed
# on a keyboard
print("Print character with hex value of 0x3E")
print("\x3E", end="\n"*2)
print("Print character with hex value of 0x3D")
print("\x3D", end="\n"*2)
print("Print character with hex value of 0xA7")
print("\xA7", end="\n"*2)
print("Print character with hex value of 0xA9")
print("\xA9", end="\n"*2)
print("Using the copyright symbol since it can't be typed")
print("Contents copyright", "\xA9", "2023", end="\n"*2)
print("Print character with Octal Value of o24")
print("\024", end="\n"*2)
print("Print character with hex value of o16")
print("\016", end="\n"*2)
# Print using unicode character and unicode name
print("Alternate Ways of printing copyright sign")
print("\u00a9")  # Unicode hex value
print("\N{COPYRIGHT SIGN}")  # Unicode character name
