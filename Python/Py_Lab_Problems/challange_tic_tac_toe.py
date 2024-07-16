# Challange: tic_tac_toe
# Allow two people to play ttt. Computer does not assist

# Global Variables

# Representation of the board as a 3 x 3 matrix
# We will use the following to indicate the state of a square
# "-" = not moved
# "x" = space occupied by "X"
# "o" = space occupied by "O"

theBoard = ["1", "2", "3", "4", "5", "6",
            "7", "8", "9"]  # Used to print the board
players = ["-", "-"]  # List that keeps the names of the players. Initially empty
whoseTurn = 0  # Represents whose turn it is -- either 0 (O) or 1 (x)
# Boolean Flag to indicate OK to make a move. Game not over.
keepPlaying = True
whoWon = -1  # Represents state of the game
# -1 = no winner (the initial state of the game)
# 0 = winner was "O"
# 1 = winner was "X"

numberOfMoves = 0  # Tracks the number of moves in the game.
# 0 = game has not started
# 9 = all moves made

# ----------- End of Global Variables -------------------

# ----------- Game Functions
# iterate through all elements and set values


def set_up_board():
    print("Setting up initial board...")
    print("'-' means the space is empty")
    for i in range(0, 9):
        # mark each space in the board with no move
        theBoard[i] = "-"+"("+str(i+1)+")"

# Display board
# Lots of work to format display so that it looks like a board
def print_board():
    print("Here is the current state of the board:", end="\n\n")
    for i in range(0, 9):
        print("  |  ", end="")
        # spacing if the square has NOT been moved in
        if len(theBoard[i]) > 1:
            print(theBoard[i], end="")
        else:  # if the square has been moved in
            print(f" {theBoard[i]}  ", end="")
        # Take care of the end of the row
        if (i+1) % 3 == 0:  # last one in the row
            print("  |", end="\n")
    print("\n", end="")

# Determine who will go first
def get_players_names():
    print(f"X will go first.")
    players[0] = input("Who wants to be 'X' and move first? >>")
    players[1] = input("Who wants to be 'O' and move second? >>")

# Make a move
def makeMove(person):
    # Asks for and makes a move for person
    # Checks to see if it is a valid move
    # if move is valid, changes the board  and prints the board
    # called with: person making the move
    # returns: a list [result, message]
    print(f"It's your move {players[person]}")
    move = int(input(f"What square would you like to move in? >>>  "))
    # Check validity of move
    #
    if move > 9 or move < 0:
        # Check to see if the move was in a legal square
        return [False, "your move must be a valid number of the squares 1 - 9. Try again"]
    elif ("X" in theBoard[move-1]) or ("O" in theBoard[move-1]):
        # Check to see if the requested move was in an occupied space
        return [False, "that square is not available."]
    else:
        # 2. Make The Move. Checks for valid move completed
        # This is a valid move
        if whoseTurn == 0:
            theBoard[move-1] = "X"  # Move is OK so we mark the board
        else:
            theBoard[move-1] = "O"
        print_board()  # and print the board so you can see the results
    return [True, "That was a legal move"]

# Checks all valid combos to see if there is a winner
def checkForWinner():
    keepChecking = True # flag indicating that we should continue the check process
    startCheck = 0 # indicates what cell checking should start
    # 1a. Check rows to see if they are all the same
    while (startCheck <= 6) and keepChecking:
        checkCells = theBoard[startCheck] + theBoard[startCheck +
                                                     1] + theBoard[startCheck+2]  # cells 1,2,3
        if (checkCells == "XXX") or (checkCells == "OOO"):
            print(f"*** {players[whoseTurn]} is the winner on a row ***")
            keepChecking = False
            return (True)  # we can stop playing the game
        else:
            startCheck = startCheck + 3

    startCheck = 0  # Reset the check flag
    # 1b. Check columns to see if they are all the same
    while (startCheck <= 2) and (keepPlaying):
        checkCells = theBoard[startCheck] + \
            theBoard[startCheck+3] + theBoard[startCheck+6]
        if (checkCells == "XXX") or (checkCells == "OOO"):
            print(f"{players[whoseTurn]} is the winner on a column")
            keepChecking = False
            return (True)  # we can stop playing the game
        else:
            startCheck = startCheck + 1  # Check next column

    # 1c. Check diag from upper left to see if they are all the same
    if keepChecking:
        checkCells = theBoard[0] + theBoard[4] + theBoard[8]
        if (checkCells == "XXX") or (checkCells == "OOO"):
            print(f"*** {players[whoseTurn]} is the winnerr on the upper left diagonal ***")
            keepChecking = False
            return (True)

    if keepChecking:
        # 1c. Check diag from upper right to see if they are all the same
        checkCells = theBoard[2] + theBoard[4] + theBoard[6]
        if (checkCells == "XXX") or (checkCells == "OOO"):
            print(f"*** {players[whoseTurn]} is the winner on the diagonal ***")
            keepChecking = False
            return (True)  # we can stop playing the game



# -------------- Program Begins Here ---------------------------
set_up_board()  # Initialize the board
print_board()  # Print the board so that we can see it before any moves
get_players_names()  # Determine the names of the players and who will go first
# Then do the initial player setup
whoseTurn = 0  # Sets X to go first"
print(f"OK {players[0]} and {players[1]} ... here we go!")
print("Make your move using the number of the square.")
print(f"{players[0]} is 'X' and will go first")

# Main loop for the game!
while keepPlaying:
    # function returns a list result[0] = move result, result[1] message
    result = makeMove(whoseTurn) # Called with whose turn.
    if result[0]: # Move was legal  
        print(f"{result[1]} {players[whoseTurn]}")
        numberOfMoves += 1  # One move legal move was made
        if numberOfMoves > 2:  # check for winner after 2 moves
            if checkForWinner():
                keepPlaying = False  # a Winner was found. Stop Playing
        if whoseTurn == 0:  # change to the next player because the move passed the test
            whoseTurn = 1
        else:  # whoseturn == 1
            whoseTurn = 0  # change to the next player
    else:  # move was not successful
        print(f"Nope. You can't make that move because {result[1]}")
# --------- End of main game loop        
print(f"Thanks for playing!")
