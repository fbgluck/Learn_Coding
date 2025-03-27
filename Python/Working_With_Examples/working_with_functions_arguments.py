# Working_with_functions_arguments
# This program demonstrates the use of a function that has arguments passed to it

# Function Defs
def calculate_score(swords, diamonds, hammers):
	pointsForSwords=3
	pointsForDiamonds=12
	pointsForHammers=9
	print(f'Calculating Score...')
	total_score = (swords*pointsForSwords) + (diamonds*pointsForDiamonds) + (hammers * pointsForHammers)
	return total_score
# END FUNCTION DEF
################################################
# Program execution begins here
print(f'The Quest begins')
numberOfSwords = 3
numberOfDiamonds = 2
numberOfHammers = 7
print(f'The Quest has ended')
print(f'Your treasure consists of {numberOfSwords} swords, {numberOfDiamonds} diamonds and {numberOfHammers} hammers.')
# my_score=calculate_score(3,2,7)
my_score=calculate_score(numberOfSwords,numberOfDiamonds, numberOfHammers)
print(f"Your total score is {my_score}")
	