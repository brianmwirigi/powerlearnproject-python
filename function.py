# function:
# a block of code (set of statement) to perform a task
# these block of are given a uniques name for identification

# type
# user defined function
# in-built functions
# __user defined function__
# geneal syntax
# def functionname(parameter):
# statement to perform the task

def greeting():
    print("Jambo Africa. welcome to PLP")

# calling a function
# syntax
# functionname(argument): calling a function with parameters
# functionname() :alling a function without parameters


greeting()  # calling a function without parameter and must be called outside where it was declared

# creating a function with parameters


def details(firstname, lastname):
    print(
        f"Hello. + {firstname} + {lastname}. i hope you are learning somethin new today")

    print(details("brian", "mwirigi"))

# create a function to calculate the area of a circle or rectangle or any shape


def area_of_circle():
    radius = float(input('enter the radius'))
    area = 3.142 * radius

    print(area_of_circle())

    # scope
    # 4 types of scope
    # local scope

    def get_total_local(a, b):
        total = a + b  # local scope variable because it is declared inside function
        return total
        print("our total is:", get_total_local(12, 15))

        # encloded scope return a function inside a function

        def get_total_enclosing(num1, num2):
            total = num1 + num2

            def double_int():
                double = total * 2  # local variable
                print(double)
                double_int()
                return total
                return ("after double operation")

                print(get_total_enclosing(20, 30), "the sum is ")

            # global scope
            # built-in scope
