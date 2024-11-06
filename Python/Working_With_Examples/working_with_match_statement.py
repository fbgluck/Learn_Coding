# Match Statement
# New in Python 3.x. Implements the "switch" functions of other languages" 
# Better than if / elseif
gradelevel=input("What class are you currently in? ")
match gradelevel:
    case "Freshman":
        print("You have a long way to go...")
    case "Sophomore":
        print("Only three more years!")
    case "Junior":
        print("You're almost there...")
    case "Senior":
        print("There is light at the end of the tunnel")
    case _:  # Fall through condition in case no matches above
        print("Are you sure you are even a student here?")
print("Thanks for playing!")
