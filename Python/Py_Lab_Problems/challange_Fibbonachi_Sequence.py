# Fibbonachi Sequence
print("\x0c")
# Ask for how many numbers you want to calculate
finishLoopCount = int(
    input("How many values in the sequence do you want to count? "))

# assign the first two numbers
currentLoopCount = 1
counter = 1
firstNumber = 0
secondNumber = 1
# calculate the first item in the sequence
result = firstNumber + secondNumber
# print the first sequence
print(
    f"Sequence member: {currentLoopCount} - Value: {firstNumber} + {secondNumber}\t\t{result}")
currentLoopCount += 1
# Loop to calculate the remainder of the numbers
for counter in range(counter, finishLoopCount, 1):
    # adjust for the next item in the sequence
    firstNumber = secondNumber
    secondNumber = result
    result = firstNumber + secondNumber
    # print the output
    print(
        f"Sequence member: {currentLoopCount} - Value: {firstNumber} + {secondNumber}\t\t{result}")
    currentLoopCount += 1
print("Fibonacci is done...")


# canculate the next number in the sequence
# add the two numbers
# print the output
