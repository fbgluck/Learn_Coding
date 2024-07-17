# Devowling Exercise
'''
Write a program that will do the following:
Assign the following string to a variable: "The story so far: in the beginning, the universe was created. This has made a lot of people very angry and been widely regarded as a bad move."
Iterate through the string and
Count the number of vowels (a,e,i,o,u) in the string
Replace each vowel with an asterisk.
Print the length of the string
Print a total of the number of each vowel that you found.
Print the percentage of each vowel in the string
'''
# The original string  that will have its vowels replaced
source_string = "The story so far: in the beginning, the universe was created. This has made a lot of people very angry and been widely regarded as a bad move."
vowels= "aeiou" 
vowel_count = [0,0,0,0,0] # each member in the list is the count of the corresponding vowel
result_string ="" # the final string where all the vowels have been replaced with *

source_string_length = len(source_string) # the length of the original string

for pointer in range (0,source_string_length): #Iterate through each character in the string

    target_character = source_string[pointer] #pick out the character from the original string that is to be examened
    if target_character in vowels: # if the picked character is a vowel (it is in the list of vowels)
        # find out what vowel it is
        target_position = vowels.index(target_character) # The position in the list of vowels tells us what vowel it is"
        vowel_count[target_position] = vowel_count[target_position] + 1 # tally up one more of the vowel found       
        result_string=result_string + "*" # then replace it in the original string with *
    else:
        result_string = result_string + target_character # Otherwise just keep the letter in the result string.
#End of for loop


print(f"The replacement is complete...\n")
print(f"The original string was:\n{source_string}\n")
print(f"The length of the original string is: {source_string_length} characters.\n")        
print(f"The result string is:\n{result_string}\n")
print(f"The length of the result string is: {len(result_string)} characters.\n") 
print(32*"-")
for i in range(0,5):
    print(f"The letter '{vowels[i]}' occured {vowel_count[i]} times which was {vowel_count[i]/source_string_length:.2%} percent of the total length ")