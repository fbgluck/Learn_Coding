# This sample will use the python csv library to read an existing CSV file into a dictionary
import csv # a library that allows you to easily read CSV files
# Use system dialog to allow user to select csv file to read
# use GUI here to show a file picker.
filename = './working_with_examples/weekly_transaction_data.csv'
with open(filename) as csv_file: # create an pointer to the csv_file
    csv_reader = csv.reader(csv_file, delimiter=',') #create an object from the file
    print (csv_reader)
    lineCount = 0 # holds the line number just read
    for row in csv_reader: #creates a list from the row
        if lineCount == 0: # we are reading the first line
            print(f"Header row contains {row}") #display other data we got
            lineCount=lineCount+1 
        else:
            print (f"Row {lineCount} contains {row}") #display the data we got
            # process the data here.
            lineCount=lineCount+1

# Create a report that shows the total dollars spent by credit card for the items in this file
# Your sample output should look like:
'''
Weekly Credit Card Report Sorted by Credit Card Type

Card Type       Total Amount
---------       -------------
MasterCard          $xxx.xx
Visa                $xxx.xx
American Exp        $xxx.xx

-----------------------------

Total CC Purchases:     $xxx.xx
Total CC Transactions:      xxx
Average CC Trans:       $xxx.xx

'''