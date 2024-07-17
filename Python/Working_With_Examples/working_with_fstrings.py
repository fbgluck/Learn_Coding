# Ref:https://realpython.com/python-f-strings/
# https://zetcode.com/python/fstring/

# This is code that shows the ins and outs of f strings
import numbers

print ("-------------- Floating Point Numbers -----------")
first = "First"
second = "Second"
combined = f"{first} then {second}" #Creates a new formatted string
print(combined)

# Formatting Floating Point numbers (:.)
val = 12.3

print(f'2 decimal places: {val:.2f}')
print(f'5 decimal places: {val:.5f}')
print ("----------- Columns ----------------------")
# f strings in columns :n  where n = number of spaces in the column
for x in range(1, 11): # ** is the exponent operator
    #Note: ^ is bitwise OR ** is exponentiation
    print(f'{x:2} {(x**2):3} {(x**3):4}')

print("---------- Right Justified Strings-----------------------")
# f strings justified to the right (:>) n = column width
# Note: default is left justified

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')

print ("---------- Formatting Currency using the .format property-----------")
amount = 123456.78
currency = "${:,.2f}". format(amount) 
print(currency)
print (f'${amount:,.2f}')  # can combine two or more formatting but needs to be in a specific order.
# format_spec ::= [[fill]align][sign][#][0][width][grouping_option][.precision][type]



