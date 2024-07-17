# This is a program that will translate a number into
# its English equivalent that can be used when writing
# a check
# *********************************************
import math
# Functions


def num_to_english(num, digit_place, result_string):
    """ Translates a number to english equiv
        Inputs:
            Num -  Number to be translated as integer
            Digit place - place (e.g tens = 2, hundreds = 3... etc) as integer
        """
# Modulus: % returns the remainder when the first operand is divided by the second
    idx = num % 10  # gives you the whole number of the next place
    if idx >= 1 and idx <= 9 and digit_place == 1:  # Process twenty through ninety
        result_string = numeral_names[idx] + \
            places[digit_place] + result_string
        # print(f"{numeral_names[idx]} {places[digit_place]}")
    else:  # otherwise, work on hundereds forward
        results_string = numeral_names[idx] + places[digit_place]

    if num/10 > 1:  # We have more digits to process
        digit_place = digit_place + 1  # Process the next place
        # // is the operation that returns the whole number of a division
        num_to_english(num//10, digit_place, result_string)
    return(result_string)


# Initialize variables
ones_place = 0
english_string = " and "
# Dictionary of Names
numeral_names = {
    "00": "zero",
    "0":"zero",
    "01": "one",
    "1":"one",
    "02": "two",
    "2":"two",
    "03": "three",
    "3": "three",
    "04": "four",
    "4": "four",
    "05": "five",
    "5": "five",
    "06": "six",
    "6": "six",
    "07": "seven",
    "7": "seven",
    "08": "eight",
    "8": "eight",
    "09": "nine",
    "9": "nine",
    "10": "ten",  # ten,zero
    "11": "eleven",  # ten one
    "12": "twelve",  # ten two
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"

}
tens_places = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

places = {
    1: "",
    2: "tens",
    3: "hundred",
    4: "thousand",
    5: "hundred thousand",
    6: "million",
    7: "hundred million"
}
####
# Input the number to be translated
text_numeral = input("What is the amount of the check?")
print (f"You entered - {text_numeral}")
# Check to see if string has a decimal point
decimal_location = text_numeral.find(".")
if decimal_location < 0:
    print(f"ERROR - You input {text_numeral}. This number must contain a decimal point")
# Check to see that decimal point has only two characters following it
if text_numeral[-3] != ".":
    print(f"ERROR - Only two numbers can follow the decimal point")

# Split string at the decimal point into two parts
splitString = text_numeral.split(".")
whole_part=splitString[0]
decimal_part=splitString[1]
# Check that both parts have only numerical values
if not(whole_part.isnumeric()):
    print(f'Whole part of your entry {whole_part} can only be numeric')
if not(decimal_part.isnumeric()):
    print(f'Decimal part of your entry {decimal_part} can only be numeric')

print(f"Left of number: {whole_part}")
print(f"Right part of number: {decimal_part}")

# append the decimal part to the result string
english_string = english_string + decimal_part +"/100"

# start working on the whole part of the number
print(f"processing: {whole_part[-2:]}") # find the rightmost two digits

# Numbers below twenty (e.g. the 'teens') are handled differently than the rest of the numbers
if int(whole_part[-2:]) < 20: # handle numbers below twenty
    # Retrieve the numeral name by the right 2 digits of the whole number part
    english_string = numeral_names[whole_part[-2:]] + english_string 
    print (english_string)
else: # handle >=20
    if whole_part[-1:]=="0": # First process 20, 30, 40, 50 ...90
        english_string = tens_places[whole_part[-2]] + english_string
    else: # then the other numbers with two places (e.g. 23, 64 ...etc)
        english_string = tens_places[whole_part[-2]] + " " + numeral_names[whole_part[-1]] + english_string
#If there is a hundreds place, process it
if len(whole_part) > 2:
    print(f"Length of whole part: {len(whole_part)}")
    for numDigits in range (3,len(whole_part)+1):
        print (f"Processing digit {numDigits}")
        #if numDigits == 3:
            #print(f"NumDigits: {numDigits}")
            #print(f"whole part: {str(whole_part[-(numDigits)])}") # pick out the part of the string
            #print (f"Numeral name: {numeral_names[str(numDigits)]}")
        english_string = numeral_names[str(whole_part[-(numDigits)])] + " " +  places[(numDigits)] +" " + english_string

        
  
print(f"result: {english_string}")                                                                        