# This program is a guessing game that demonstrated binary search 
# Author: Fredric Gluck
# Date: 29 March 2024
# Version: 
# -----------------------------------
# binary search is the process of dividing a range in half each time then choosing the midpoint of the range for the guess. After
# each failed guess, the range of available numbers to choose from gets smaller by half. Binary search works assuming the list is always
# sorted from lowest to highest.
# -----------------------------------
import random
lowerLimit = 1
upperLimit = 100 # This is the upper limit of the range og guessable numbers
# Explain the rules to the user
print(f"Computer A will generate a random number between {lowerLimit} and {upperLimit}.") 
print(f"Computer B has 5 guesses to discover the number using binary search")
# Set a variable to be the users name (input)
userName = "Computer B (the guesser)"
# Generate a random number between 1 and 100
target_number = random.randint(lowerLimit,upperLimit)
# Set a variable to be equal to the number of guesses
guess_number = 1 # the number of the guess
guessAgain = True # Flag to indicate that user did not guess number and can go again

# first guess
# First guesss is the halfway point between the lower and upper limit
guess = (upperLimit//2) # returns the returns the largest whole number less than or equal to the result (integer division)

while guess_number <= 5 and guessAgain: # Only 5 guesses are allowed
    # Display the current guess and guess number
    print (f"For guess number {guess_number}, {userName} guesses {guess}")

    # Check to see where the guess is relative to the target number     
    if guess > target_number:
        guess_number = guess_number +1 #add one to the guess
        print (f"You guessed {guess} and that's too high!")
        upperLimit = (guess-1) # set up for next guess
        print(f"I'm going to now guess a number between {lowerLimit} and {upperLimit}")
        print()
        guess = guess - ((upperLimit-lowerLimit)//2)
    elif guess < target_number:
        guess_number = guess_number +1 #add one to the guess
        print (f"Your guess of {guess} is too low")
        lowerLimit=guess+1
        print(f"I'm going to now guess a number between {lowerLimit} and {upperLimit}")
        print()
        guess = guess + ((upperLimit-lowerLimit)//2)
    elif guess == target_number:
        print(f"You got it in {guess_number} guesses. The number was {target_number}")
        guessAgain=False # Stop the game.
    
# User has run out of guesses
    if guess_number > 5:
        print (f"Sorry {userName}. You didn't get it. You used up all of your {guess_number-1} guesses. Computer chose the number {target_number}")

print("Thanks for playing!")





