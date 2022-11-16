# using while and elif loop

print("to win the game you have to guess the number between 1 to 9")
guess = int(input("input number "))
number = 4
while number != guess:

    if number == 4:
        print("well guessed")

    elif number >= 0 and number <= 3:
        print("wrong guess")

    elif number >= 5 and number <= 9:
        printf("wrong guess")

    else:
        print("out of range")
