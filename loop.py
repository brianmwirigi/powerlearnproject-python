# the loop
# the while loop in python is used to iterate over a block of code aslong as the test expression (condition) is true
# syntax of while loop in python

# while test_expression:
# body of while
# sum = 1+2+3....+n

n = 10
sum = 0
# integer counter with an (indexing variable)
x = int(input('enter a number '))

while x <= n:
    sum = sum+x
    print("the sum is", sum)
    x = x+1  # update counter x += 1
