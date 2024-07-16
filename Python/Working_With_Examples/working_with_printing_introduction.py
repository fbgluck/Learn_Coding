# Python program to print list 
# without using loop 
a = [1, 2, 3, 4, 5] 
# printing the list using * operator separated 
# by space 
print(*a) 
print ('*******************')
# printing the list using * and sep operator
# the * (unpack) operator passes all elements of
# the list a as seperate arguments to the print
# function 
print("printing lists separated by commas") 
print(*a, sep = ", ")
# Which is the same as....
print(a[0],a[1],a[2],a[3],a[4], sep=", ") 

# print each element on a new line 
print("printing lists in new line") 
print(*a, sep = "\n") 

# Python program to print list 
# by Converting a list to a 
# string for display 
a =["Peanut Butter", "and", "Jelly"] 

# print the list using join function() 
print(' '.join(a)) 

# print the list by converting a list of 
# integers to string 
a = [1, 2, 3, 4, 5] 

print (str(a)[1:-1]) 
