# if...elif...else statement

# grading system

# 80 - 100 ==> A
# 70 - 70 ==> B
# 60 - 69 ==> C
# 50 - 59 ==> D
# 0 - 49 ==> F

marks = int(input("Enter marks"))

if marks >= 80 and marks <= 100:  # concatination
    print("Grade is A")

elif marks >= 70 and marks <= 79:
    print("grade is B")

elif marks >= 60 and marks <= 69:
    print("grade is C")

elif marks >= 50 and marks <= 59:
    print("grade is D")

elif marks >= 0 and marks <= 49:
    print("grade is FAIL")

else:
    print("out of range")
