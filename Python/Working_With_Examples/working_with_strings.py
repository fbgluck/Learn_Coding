# Visual Studio Code hints ....
#  CTL+K+C == comment out code
#  CTL+K+U == remove comment
# # Samples of Python Strings
# first_name = 'Fredric'
# last_name = 'Gluck'
# login_prompt = 'Please enter your ID:'
# password_prompt= 'and now enter your password:'
# user_ID=input(login_prompt)
# password_entered=input(password_prompt)
# print("I know who you are now. Your USERID is:")
# print(user_ID)
# print(f"Your password is: {password_entered}")

# ---------- STRING SLICING ---------#
slice_string = 'abcdefghijklmnopqrstuvwxyz'
# Built In Length Function
print(f'The length of slice_string is: {len(slice_string)} characters.')
# Slicing Strings (Remember: String The first character is [0])
print(f'The 4th position is {slice_string[4]}')
print(f'start at 0 stop before 5 position is {slice_string[0:5]}')
print(f'Start at 1 stop before 6 slice is {slice_string[1:6]}')
# ----------- SAMPLE CODE FOR WORKING WITH STRINGS --------------# 
print(f'**** SAMPLE CODE FOR WORKING WITH STRINGS')

reaction = 'totally weird'
# Print the third (0,1,2,3) char from the left
print (f'\n#1:: The third index char from the left is {reaction[3]}') 
 # Print the fourth (-1, -2, -3, -4) from the right
print (f'\n#2:: The fourth index char from the right is {reaction[-4]}') # Print the fourth (-1, -2, -3, -4) from the right
 
# Demonstrates how to work with strings
# *** Copy this code to your own file!
# *** Uncomment what you want to test
# *** Can't mix indexes -- the numbers need to be all positive or all negative
test_string = '0123456789ABCDEF'
print(f'\n#3:: The string we are working with is: {test_string}')

print("\n-----Index from the left of the string -----")
print(f"#4:: *** The 6th character from the left is: {test_string[5]}") 
print(f"#5:: *** The 10th character from the left is: {test_string[10]}") 

print("\n-----Index from the right of the string -----")
print(f"#6:: *** The 4th character from the right is: {test_string[-4]}")
print(f"#7:: *** The 9th character from the right is: {test_string[-9]}")

# # Slicing Strings
print('\n----- Slicing Strings -----')
print(f'#8:: *** This is the 0th through 2nd characters of the string: {test_string[0:3]}') 
print(f'#9:: *** This is the 4th through 5th characters of the string: {test_string[4:6]}')
print(f'#10:: *** This is the 0th through 9th characters of the string: {test_string[:10]}') 

print(f'#11:: *** This is the 4th character through end of the string: {test_string[4:]}') #leaving out the stop index, assume full string

# #Stride - take every n characters
print('\n---- String Striding ---')
print(f'#12:: *** This is every 3rd character starting at 2 and ending at 12: {test_string[2:12:3]}') 

# # What happens.....
print(f'\n#13:: What Happens and Why?')
print(test_string[3:13:]) #start=3, stop before 13, ?????
print(test_string[::1]) #What happens...

print(f'\n#14:: Miscellaneous')
# # Negative IndexError
print(test_string[-1]) #the rightmost character in the string
print(test_string[-2:-5]) #should print EDC. Default 1
print(test_string[-2:-5:-1]) #should print EDC
print(test_string[::-1]) #reverses the string every character
print(test_string[::-2]) #reverses the string every 2 characters

print(f'\n#15:: Uncomment the following to learn about IMMUTABLE strings')
## Python Strings are IMMUTABLE (They can not be changed!)
# The following will cause and error
#mystring = 'Come Here Watson, I Want You'
#mystring[4]='-' #not legal -- strings are immutable
#
# Creating a string of repeated characters
print(f'\n#16:: Easily Creating A Long String of the Same Characters')
lots_of_stars = "*" * 50
print(lots_of_stars)
print(f'\n#17::Methods to work on a string object')
# String Methods
shoutout = "what am i doing"
# STOP and see what happens when you type the .
outloud = shoutout.capitalize()
print(f'Capitalize the string: {outloud.capitalize()}')
print(f'All caps the string: {outloud.upper()}')
print(outloud.title())
print(outloud.isalpha()) # ? Are spaces counted as alpha
print(outloud.isascii())