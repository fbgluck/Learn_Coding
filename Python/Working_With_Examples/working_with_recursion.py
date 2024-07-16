#recursion (Yes, I finally got it after 30 years!)

def fn_translate(string):
# This function takes the last character of a string
# prints it and shortens the string by one character
# It keeps going  until there are no characters left
    #cut off last character
    last_char = string[-1]
    #print last digit
    print(f"I got the character: {last_char}", end='')
    # reset the string so the last character is cut off
    string = string[0:(len(string)-1)]
    print (f" and the string is now {string}")
    #recurse if there are some chars left
    if len(string)>0:
        fn_translate(string)
    return ("Done")

# ************* The Program Starts here!
tr_string = "abcde"
print(f"The original string is: {tr_string}")
# Call the function
print(fn_translate(tr_string)) 