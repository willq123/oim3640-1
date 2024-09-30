# Create function(s) that execute a simulation 10 times. Within each simulation, roll 100 dice (🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲...) and display the resulting sum.

"""
I will create 2 functions.


Function 1: one simulation, which is rolling 100 dice, which means generating 100 randome numbers, and sum up.

1. initialize a variable `total` to store the sum
2. Loop the following `n` times:
   2.1 Generate a random number between 1 and 6
   2.2 Add the random number to total
3. Print the sum

Function 2: run the roll_dice 10 times

"""
import random


def roll_dice(n=100, m=6):
    """
    Simulates rolling n dice with m sides (6 by default), and prints/returns the resulting sum, average
    """
    # print("We found the sum!")  # Fake it till make it!
    total = 0
    for i in range(n):
        random_number = random.randint(1, m)
        total += random_number
    # print(total, total / n)
    return total


def run_simulations(n=10):
    """
    Runs roll_dice simulation n times.
    """
    for i in range(n):
        print(roll_dice())


# run_simulations()

# Create a function that counts how many simulations (100 dice) it takes to reach or exceed 400


def count_simulations():
    """
    Counts how many simulations (100 dice) it takes to reach to or exceed 400.

    1. Initialize `counter` that tracks the number of simulations
    2. Loop until the sum reaches or exceeds 400
        2.1. Call the roll_dice function
        2.2. Increment counter
    3. Once we reach/exceed 400, print counter
    """
    counter = 0

    while True:
        total = roll_dice()
        counter += 1
        print(f"Simulation {counter}: {total = }")
        if total >= 400:
            break
    return counter


result = count_simulations()
print(f'After {result} simulations, the sum of 100 dice reached to 400.')