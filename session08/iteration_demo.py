# i = 0

# while i < 4:
#     print('Hi')
#     print(i)
#     i += 1

# print(i)

# for i in range(4):
#     print(i)


# Calculate the sum of all the integers from 0 to 100

# total = 0

# for i in range(11):
#     print(f"Iteration {i}:")
#     print(f"  Before adding {i}, {total = }")

#     total += i

#     print(f"  After adding {i}, {total = }")
#     print()

# print(total) # total = 55


# Create a function, sum_up_100, that calculates the sum of all the integers from 0 to 100


def sum_up_100():
    """Sums up 0 to 100, prints the sum"""
    total = 0

    for i in range(101):
        # print(f"Iteration {i}:")
        # print(f"  Before adding {i}, {total = }")

        total += i

        # print(f"  After adding {i}, {total = }")
        # print()

    print(total)


# sum_up_100()

# Create a function, sum_up(n), that takes one argument, n, calcuates the sum of all the integers from 0 to n, returns the sum


def sum_up(n):
    """
    Takes one argument, n, calcuates the sum of all the integers from 0 to n, and returns the sum
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total


# print(sum_up(100))

# Practice this with variations


# Create a funciton, sum_up_while(n), that does the same thing using while loop

def sum_up_while(n):
    """"""
    total = 0
    i = 0
    while i < n + 1:
        total += i
        i += 1
    return total

print(sum_up_while(100))


