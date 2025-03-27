# pprint library is an option
ListA = ["A1","A2","A3","A4"]
ListB = ["B1","B2","B3","B4"]
ListC = ["C1","C2","C3","C4"]
testString = "test"
# Function to print 1 or more lists that are all the same length
def printList(listsToPrint): # listsToPrint is a list of list names
    print ("you are printing", listsToPrint)
    # Break up the input string and make a list containing the names of the lists to print
    # Iterate through each list
    # use zip function to make tuples then print tuples

printItems = "ListA,ListB,ListC"
printList(printItems)
print(ListA)

# Iterate through the list so we get neat output
for i in range(0,len(shopping_list)):
   print (f'Item {i} is {shopping_list[i]}')