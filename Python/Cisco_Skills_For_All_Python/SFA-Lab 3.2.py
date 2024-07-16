# Lab 3.2.10 - The Vowel Eater
# Purpose: Input a word and output each letter that is
# not a vowel
# Author: Fredric Gluck
# Original Date: 9 May 2023
# -------------------------------------
vowel = "aeiouAEIOU"  # List of vowels
totalVowels = 0  # used to count total number of vowles
deVowled = ""    # Used to hold the devowled string

# Prompt the user to enter a phrase to be devowled
checkWord = input("Input a word or phrase >>> ")

# Figure the length of the input work so we know how much we have to check
stringLength = len(checkWord)
# start the devowling process
print("\nHere's the results of devowling... ")
# go through each letter in the world
for counter in range(0, stringLength, 1):
    # pick out the next letter to check
    nextLetter = checkWord[counter]
    if nextLetter in vowel:  # If the letter is a vowel
        totalVowels += 1  # Count one more vowel found
    else:
        # add the character to the new devowled string
        deVowled = deVowled + nextLetter

# The final summary of the task
print(30*"-")
print(f"The original string was: {checkWord}")
print(f"The length of the original string was {stringLength} characters.")
print(f"A total of {totalVowels} vowels were removed.")
print(f"The devowled string is: {deVowled}")
print(
    f"The length of the final string is {len(deVowled)} characters.")
print(f"\nAll done...\n")
