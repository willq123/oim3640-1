# Exercise 3
def my_abs_3(number):
    """
    Print the absolute value of a number

    number: an integer or a floating point number
    """
    if number >= 0:
        print(number)
    else:
        print(-number)


# my_abs_3(-10)


# Exercise 4
def my_abs_4(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if number < 0:
        return -number
    else:
        return number


# print(my_abs_4(-10))


# Exercise 5
def my_abs_5(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number

    Pseudocode: This section explains the algorithm in plain language.

    1. if number's type is an int or float:
        1.1. if the number is negative:
            return the opposite
        1.2. otherwise, return the number as-is
    2. if it is not an int or float:
        return/raise an Error
    """
    if isinstance(number, (int, float)):
        if number < 0:
            return -number
        else:
            return number
        # return my_abs_4(number)
    else:
        print("I don't know how to solve this")
        return "Wrong type of arguments"
        # raise TypeError("We do not accept this type as argument!") # a better way to handle unexpected situation


print(my_abs_5(-10))
# print(my_abs_5('abc'))

# print('Hi')
