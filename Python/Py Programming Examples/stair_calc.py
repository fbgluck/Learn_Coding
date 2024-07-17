"""
This program will calculate the dimension for a set
of stairs given the total rise and single step rise
"""
def fn_calculate_steps (total_rise,target_single_step):
    number_of_steps = (total_rise *12) / target_single_step
    print(f"Raw number of steps: {number_of_steps}")
    whole_steps = int(number_of_steps)
    print ("Whole number of steps: {whole_steps}")
    print(f"total rise in inches {total_inches}")
    number_of_steps = total_inches / target_step_rise
    print(f"raw number of steps {number_of_steps}")
    actual_number_of_steps = int(number_of_steps)
    print(f"Actual number of steps: {actual_number_of_steps}")
    total_rise / actual_number_of_steps

print ("""This will calculate the number of steps for
a total rise. 
You will be asked for three numbers:
- feet: the whole number of feet in the total rise
- inches: the whole number of inches in the total rise
- fraction: the fraction of inches in the total rise
For example: to calculate steps for a total rise of 8' 11 1/4"
you will enter:
- 8 when asked for feet,
- 11 when asked for inches,
- .25 (the decimal equivalent of 1/4) when asked for fraction
""")

target_step_rise = 7
# Get essential input from user
rise_feet = int(input ("Enter the number of feet in the total rise"))
rise_inches = int(input("Enter the number of inches in the total rise"))
rise_fraction = float (input("enter the decimal fraction of the rise"))
total_inches = (rise_feet *12) + rise_inches + rise_fraction
# Calculate step plans
fn_calculate_steps(total_inches,target_step_rise)
