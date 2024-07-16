# working_with_recursion_1
def countdown(starting, ending):
    for i in range(starting, ending, -1):
        print (f"Value is now: {i}")
    starting -=1
    if starting >= ending:
        print (f"Calling countdown with {starting} and {ending}")
        countdown (starting, ending)
        print (f"Back from calling countdown with {starting} and {ending}")

## Program starts here

print(f"Calling countdown with 5 and 1")
countdown (5,1)
print ("Back from calling countdown with 5 and 1")
print ("Program done")