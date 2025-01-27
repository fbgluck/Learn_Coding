# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} is: {sum}")
    return sum

# function call with two values
print(f"Call by position...")
add_numbers(5, 4) # 5 --> num1,  4 --> num2

print(f"Call by value...")
add_numbers(num2=4, num1=7)

# Write a function to test the first 100 numbers (1 - 100) to see if a number is prime.
# Your output should be: 
# The number <n> is (is not) prime.