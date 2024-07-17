import math

def check_if_number(is_int):
    try:
        if isinstance(is_int, int):
            print("Great... you entered a number!")
            return True
    except:
        print("Your Number is not an integer")
        return False

print ("Welcome to the Square Root Calculator!")
continue_flag=True
while continue_flag:
    no_iterations = input ("How may iterations do you want? (type 'end' to end the program) ")
    # Check if user wants to end the program
    if no_iterations =="end":
        continue_flag = False
        print("Thanks for playing")
    else:
        int_iterations = int(no_iterations)
        if check_if_number(no_iterations): # The user entered a number for iterations
            start = int("What number do you want to start at?")
            if check_if_number (start):
                # Valid inputs for all items have been entered
                for i in range (1,no_iterations):
                    print ("the square root of",start, "is", math.sqrt(i))
    continue_flag = False # We are done. End the program



