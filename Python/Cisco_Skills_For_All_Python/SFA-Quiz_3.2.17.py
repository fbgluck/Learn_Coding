# 3.2.17 - Section Quiz
# Create a for loop that counts from 1 to n
# and prints the odd numbers to the screen
print("QUESTION 1: Print odd numbers using a for loop")
for i in range(1, 11):
    if i % 2 != 0:  # Uses modulo (calculates the remainder)
        print(f"I found an odd number and it was {i}")
print("All done!")

print("QUESTION 2: Print Odd Numbers using a While Loop")
x = 1
while x < 11:
    if x % 2 != 0:  # Uses modulo (calculates the remainder)
        print(f"I found an odd number and it was {x}")
    x += 1
print("All done!")

# Question 3: Create a program with a for loop
# and a break statement.
# The program should iterate over characters in
# an email address, exit the loop when it reaches
# the @ symbol,
# and print the part before @ on one line.
# Use the skeleton below:
print("QUESTION 3 - print the first part of an email address")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
        print(ch, end="")

# Question 4: Create a program with a for loop and a
# continue statement.
# The program should iterate over a string of digits,
# replace each 0 with x, and print the modified string
# to the screen. Use the skeleton below:
print("\nQUESTION 4: Replace characters")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

print(30*"-")
# Question 6: What is the output of the following code?
print("QUESTION 6:")
n = range(4)
for num in n:
    print(f"num is:{num} and num-1 is {num - 1}")
else:
    print(f"this is the else clause: {num}")  # This will always print
