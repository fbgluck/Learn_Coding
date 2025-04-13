# Play loop demonstration.
# This is a demonstration of how you can program a "play again" loop that
# allows a program to be repeated until the user stops it.
continuePlay = True # first time through
 
# Game loop starts here
while continuePlay == True: # game loop 
    print("continue playing") #game code goes here
    askToPlay = input("Play Again (y/n)") #Ask if user wants to continue
    # add code to convert input to lower case
    # add code to check to see they entered one letter
    if askToPlay =="n":
        continuePlay = False #signals end of play
# End of While Loop
print ("Thanks for playing")