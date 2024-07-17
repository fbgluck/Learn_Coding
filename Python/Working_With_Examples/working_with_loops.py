# Sample code for Loops
# Uses the range(start, stop, interval) function
# Stop must have a value. If one arg is supplied, it is assumed to be stop
# Start default = 0
# Interval default = 1

# The range function with defaults
print("Count from 0 to 4 (5 items) using the range() function")
for value in range(5):
    print(f"The value is now {value}")
input("Type ENTER to continue or ^C to break..")
print("Demonstration of 'for' statement with 'range'")
print(30*"-")
print("Hello World")
jump = int(input("What is the interval of jump? "))
for i in range(1, 100, jump):
    print("The value is now", i)
print("loop is done")
input("Type ENTER to continue..")

# For Loop
print(30*"-")
print("Using a For Loop and the range function to count")
startCounting = 1
startCounting = int(input('Where do you want to start:'))
# Range is a built-in function that will interate from start to stop
for i in range(startCounting, startCounting+10):
    print(f'The number is {i}')
input("Type ENTER to continue..")
# Sample Boolean
print(30*"-")
print("Build a light switch")
switch_state = True  # set this variable to Boolean True
if switch_state:
    print("Lights Are On")
else:
    print("Lights are off")

input("Type ENTER to continue..")

# While Loop
print(30*"-")
print("While loop demonstration")
count = 0
while count < 10:
    print(f'The Count is now {count}')
    count += 1
print(f'I completed the while loop')

input("Type ENTER to continue..")

# From section PE1-3.2.1
print(30*"-")
print("Another While Loop Demonstration")
loop_counter = 1
while loop_counter < 7:  # the test is performed here
    print(f"The loop counter is {loop_counter}. ")
    print(f"Let's continue the loop..")
    loop_counter += 1  # increment the counter
print(f"We are out of the because 'loop_counter' is no longer less than 7")


input("Hit ENTER to see an infinite loop! CTL+C will stop the loop")
# Infinite While loop - test condition is never met
loop_counter = 0
while loop_counter < 7:
    print(f'The value of loop_counter is {loop_counter}')
    loop_counter -= 1  # loop counter will always be < 7
# end of the loop
print("Loop is done")
