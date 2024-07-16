# This program shows a way to make a menu and have code
# executed from a menu

# Import Libraries
from datetime import date, datetime
import os
# OS functions
os.system('cls')

# Set up Functions


def fn_show_menu():
    """
     Display menu choices
     Parameters: none
     Returns: none
    """
    now_time = datetime.now()
    # print(x.strftime("%B %d, %Y"))
    print(f"Main Menu -- It is now", now_time.strftime("%B %d, %Y"))
    print("1: Add two numbers ")
    print("2: Multiply two numbers ")
    print("3: Return the next number in the sequence ")
    print("4: Convert Minutes to Seconds ")
    print("5: How long have you been alive? ")
    print("Q: Quit the program ")


def fn_process_menu_choice(choice_made):
    """ 
    Processes the choice that the user made
    Parameters: string - choice that the user made from prompt
    Returns: none
    """
    if choice_made == "1":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        print(
            f"The Result of adding {x} and {y} is {fn_add_two_numbers (x,y)}")
    elif choice_made == "2":
        x = input("Input the first number: ")
        y = input("Input the second number: ")
        print(
            f"The Result of multiplying {x} and {y} is {fn_multiply_two_numbers (x,y)}")
    elif choice_made == "3":
        starting_base = input("Please enter a number to be increased by 1: ")
        print(
            f"The number you entered was {starting_base}, the next number is {fn_nextNumber(int(starting_base))}")
    elif choice_made == "4":
        mins = input(
            "Enter the number of minutes to be converted to seconds: ")
        print(
            f"There are {fn_min_to_seconds(int(mins))} seconds in {mins} minutes")
    elif choice_made == "5":
        birth_year = input('What year were you born (4-digits)? ')
        birth_month = input('what month number of the year were you born? ')
        birth_day = input('What day of the month were you born? ')
        fn_how_long(int(birth_year), int(birth_month), int(birth_day))

# Functions called by the menu are here


# Challenge no. 1 -- Build a function that finds the sum of two numbers
def fn_add_two_numbers(first_no, second_no):
    result = int(first_no) + int(second_no)
    return result

# Challenge no 2 -- Build a function finds the product of two numbers


def fn_multiply_two_numbers(first_no, second_no):
    result = int(first_no) * int(second_no)
    return result

# Challenge no 3 -- Build a function that increments a number


def fn_nextNumber(base):
    return base+1

# Challenge no 4 -- Convert number of minutes into seconds


def fn_min_to_seconds(mins):
    return mins * 60
# Challenge no 5 -- Calculate how long you have lived


def fn_how_long(my_year, my_month, my_day):
    # Creates a datetime object from the input
    birth_date = datetime(my_year, my_month, my_day)
    # Creates a datetime object from the current time
    now_date = datetime.now()
    nice_date = now_date.strftime("%B %d, %Y")  # For formatting the output
    delta = abs(now_date - birth_date)  # delta is created as a time object
    print(f"\nIt is now: {nice_date}")
    print(
        f"You have been alive for a total of {delta.days} days")
    print(
        f"You have been alive for a total of {delta.seconds} seconds")
    input("Enter to continue...")


# *************** Program Begins Here ************************************
continue_flag = True  # Used to indicate if the menu should be redisplayed
while continue_flag:
    fn_show_menu()  # Display the menu
    # Get the input and covert it to uppercase
    user_option = (input("Make a Choice: ")).upper()
    if user_option == "Q":  # user indicated end program
        continue_flag = False  # set the flag to stop the program
        print("Program Quits!")
    if continue_flag:
        # Process the menu choice
        fn_process_menu_choice(user_option)
