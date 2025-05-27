# Pseudocode Planning:
# 1. Start with i = 0
# 2. Loop from i = 0 to i = 9 (a total of 10 iterations)
#    a. For each iteration:
#       i.   Increment i by 1
#       ii.  Compute the triangle number for current i
#            - A triangle number is the sum of integers from 1 to i
#       iii. Print the triangle number

i=0 #start with i=0
#start a loop to count the triangle numbers
for i in range(0,10):
    i += 1 #i=i+1 for each loop
    triangle_number=sum(range(1,i+1)) #count triangle number for each i by summing up 1 to i
    print(triangle_number) #print the results

