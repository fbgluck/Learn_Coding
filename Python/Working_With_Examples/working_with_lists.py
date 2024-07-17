# # Sample Code for Working With Lists and their Methods

## Lists are a built-in Python Data Type that are used to 
## store multiple items in a single variable.

# ------- This stuff is used to make the output readable ------------------------
line_sep = '*'*30 #This is a global variable known to all functions
def fn_line_seperator():
   print(f"\n{line_sep}\n")
# ------------------------------

## -- PROGRAM STARTS HERE --

# Syntax used to Define A List
major_authors=['Lee','Orwell','Fitzgerald','Salinger']
mixed_list=['First',1,'Second',2,'Third',3]

# Using two lists together
shs_football_scores= [27,12,17,15,0]
shs_football_opponents=['York','Noble','Portland','Massabesic','Marshwood']
print (f'The score against {shs_football_opponents[1]} was {shs_football_scores[1]}')
fn_line_seperator()

# How would you print a scorecard for SHS football for these 5 games. Hint -- user iteration / for / range



# The first list entry is item "0"
print (major_authors[3]) #gives you the fourth entry in the list
fn_line_seperator()

# Lists can be manipulated and queried (added to, subtracted etc using 'methods')
#*********** .append method *****************

#.append = appends a value to a list
shopping_list=['apples','bacon','carrots','doughnuts']
new_list = shopping_list.append('eggs')
#new_list is empty because .append method modifies in place -- a new list is not created.
print(f'new_list is now: {new_list}')
print(f'shopping_list is now: {shopping_list}')
fn_line_seperator()

# .index = returns the location of the first matching value in the list
print(f'Our shopping list is now: {shopping_list}')
location=shopping_list.index('bacon')
print (f'bacon appears in the list as item number {location}')
fn_line_seperator()

# .count counts the number of times an item is in a list
# Good for determining if an item is or is not in the list?
fruits = ['apple', 'banana', 'cherry']
x=fruits.count("cherry") # .count returns the number of times an item in in a list
if x==0:
   print (f"Item is not in the list") # count was 0
else:
   print (f"Item was in the list {x} times")
     
# We can assign one list to another variable to make a copy of it
new_list = shopping_list
print(f'shopping_list is: {shopping_list}')
print(f'new_list is now: {new_list}')
fn_line_seperator()

#**** .insert METHOD *********************
# INSERT Item in list using Index
# .insert(<at_index>,<item>)
shopping_list.insert(2,'spaghetti')
print(f'modified shopping_list is now: {shopping_list}')
fn_line_seperator()

# ********* .extend Method *******************
#.extend method -- extends a list from the print
# This is an 'iterable' meaning it will do the
#.extend over the list of items 
shopping_list = ["item_one", "item_two"]
shopping_list.extend(['flour','grapes','iodine'])
print (f'Extended shopping_list is now: {shopping_list}')
# Iterate through the list so we get neat output
for i in range(0,len(shopping_list)):
   print (f'Item {i} is {shopping_list[i]}')
fn_line_seperator()

# # ************** .pop Method *******************
# ## removing (.pop) -- takes the index of the item. Returns the item that was removed.
shopping_list.pop() #no arguments, removes the last item
print ('The list is shorter now ....', shopping_list,'\n',30*'-','\n')
## .pop with an index of 0
shopping_list.pop(0)
print ('The item at index 0 is gone', shopping_list,'\n',30*'-','\n')

# # ***** .remove Method *************
# ## .remove - removes the item with a specified value from the list. Works in place
shopping_list.remove('carrots')
print('Our shopping list is shorter..', shopping_list,'\n',30*'-','\n')
## EXPERIMENT -- what happens if we remove an item not in the list
# shopping_list.remove('zzyzx')

# # ***********. clear method *****************
# ## clear removes whatever is in the list
shopping_list.clear()
print('The list is now empty... see...', shopping_list,'\n',30*'-','\n')

# ## Reset the list
shopping_list=['apples','bacon','carrots','doughnuts']
print(shopping_list,'\n',30*'-','\n')
# # Find what index a particular item is in a list
print('The item you are looking for is index ...', shopping_list.index('carrots'),'\n',30*'-','\n')
# You can also supply start and Stop
# print('We can search from start to stop..', shopping_list.index('carrots',0,2),'\n',30*'-','\n')

# ## IN keyword -- returns true or false
print('carrots' in shopping_list,'\n',30*'-','\n') #used with list
print ('hello' in 'hello world','\n',30*'-','\n') #used in string
print('Are Carrots in the list?..',
   'carrots' in shopping_list[0:2],
   '\n',30*'-','\n')

# ## Count how many times an item occurs
target = 'carrots'
print(target.title(),
 'occurs '
 ,shopping_list.count(target),
 ' times',
 '\n',30*'-','\n' )

# This will not work.... why??
target = 'r'
print(f'{target} occurs {shopping_list.count(target)}times')
fn_line_seperator

# use count with strings
target_string = 'carrots'
find_string="r"
print(find_string,
 'occurs',
 target_string.count(find_string),
 'times in',
 target_string,
 '\n',30*'-','\n')

# #sort method
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
print('The list is...',test_list,'\n',30*'-','\n')
test_list.sort() #modifies in place. No new list created
print('The sorted list is now:',test_list,'\n',30*'-','\n')
test_list.sort()

# # Buit in function sorted()
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
new_list=test_list.sort()
print('New_list is now:',new_list,'\n',30*'-','\n')
test_list=['Zane','Jean','Wally','Phil','Fred','Stacey','Albert']
print('We have reset the list',test_list,'\n',30*'-','\n')
print('But if we use the sorted() function the list is sorted ...', sorted(test_list),'\n',30*'-','\n')
print('...and the original list is not touched',test_list,'\n',30*'-','\n')

# # .copy method -- copies the list and returns a new list
new_list=test_list.copy()
print('I just made new copy... here it is:',new_list,'\n',30*'-','\n')

# # reverse the list in place
test_list = ['c','g','a','w']
print('Our new list is:',test_list,'\n',30*'-','\n')
test_list.reverse()
print('Reverse The List:', test_list,'\n',30*'-','\n')

# # you can use a sorted, reversed basket
test_list = ['c','g','a','w']
test_list.sort()
test_list.reverse()
print('The sorted, reverse list is: ',test_list,'\n',30*'-','\n')

# Generating Lists
# The following will create a list with the squares of 4 - 6
numbers = [x*x for x in range(4,7)]
print (numbers)