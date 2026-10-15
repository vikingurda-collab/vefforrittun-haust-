#When the pizzaboxes are open, the number of pizza slices can be counted, and they are 
# in total. The number of people living in Ómar’s household are 
#. The residents are all very hungry and eat as much as they possibly can, but the rules of the household state that all residents must get an equal number of slices. The rule has a flaw, since there may be some food left over which nobody eats. How many slices will be left over?

#Input
#Input consists of two lines. The former line consists of a single integer 
#, the number of slices. The latter line consists of a single integer 
#, the number of residents in Ómar’s household.

#Output
#Print one integer, the number of slices left over.
n = int(input())
m = int(input())

s = n % m
print(s)