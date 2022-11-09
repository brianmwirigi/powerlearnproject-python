# syntax of wj=hile loop in python
# break statement: with the break statement we can stop the loop if the while condition is true

# why do we increment in a while loop before the if statement
x = int(input("input a number"))
while x < 10:
    print(x)
    if x == 3:
        break
    x = x + 1  # x + = 1
