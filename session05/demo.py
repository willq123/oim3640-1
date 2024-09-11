r_1 = 3
r_2 = 4.3
r_3 = 9.11


# area_1 = 3.14159 * r_1**2
# area_2 = 3.14159 * r_2**2
# area_3 = 3.14159 * r_3**2

# print(area_1)
# print(area_2)
# print(area_3)

"""
radius: parameter variable
"""

def calc_area(radius):
    """
    (This is docstring, which is a short summary of this function)

    Calculate the area of a circle with radius value provided, then return it.
    """
    pi = 3.14
    area = pi * radius**2
    # print(area) # this will print the area in terminal
    # if the function does not explicitly return a value, it will return None.
    return area


area_1 = calc_area(r_1) # r_1: argument
area_2 = calc_area(r_2)
area_3 = calc_area(r_3)

# add two areas togethers
total = area_1 + area_2 + area_3
print(total)


# Define a function that takes one argument and return the double of the argument's value

def double(a):
    """return double of input's value"""
    return a * 2

print(double(10))
print(double(-5))


# given a radius of 3, calculate the area of a circle, the radius is the double of the original radius

radius = 3
new_r = double(radius)
result = calc_area(new_r)
# print(result)

print(calc_area(double(radius)))