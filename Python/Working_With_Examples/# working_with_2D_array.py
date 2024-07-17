# working_with_2D_array
# Python doesn't do arrays so you use a lists in lists (also called nested lists)
#
# I like defining 2D arrays this way only because it helps me visualize
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
 ]
# we iterate though each element 
for i in range(len(a)):
    for j in range(len(a[i])):
        print (a[i][j],end=' ')
    print()
