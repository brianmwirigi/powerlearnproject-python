# syntax of wj=hile loop in python
# continue statement: with the continue statement we can skip the condition of the loop if the while condition is true

# why do we increment in a while loop before the if statement
x = int(input("input a number"))
while x < 10:
    print(x)
    x = x + 1  # x + = 1
    if x == 3:
        continue
print(x)
