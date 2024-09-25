# for i in range(1, 10):
#     if i % 3 == 0:
#         continue
#     print(i)

# print("Hi")

# print("😊" * 5)


# for i in range(5):
#     print("😊", end="")
# print()


# def f(n):
#     for i in range(n):
#         print("😊" * i)


# f(5)
# f(3)

# n = 5
# while n != 0:
#     print(n)
#     n = n - 2


# When to use what (for vs. while)

# 1. Use for loop
# 1.1 when you know the exact number of iterations

# for i in range(4):
#     print('Hi')


# 1.2 When you need to iterate over a collection/sequence, such as a string, list, dict, tuple, set, ...

# for whatever in 'felipe':  # a string
#     print(chr(ord(whatever)+2))

# for num in [1, 2, 5, 854, 65]: # a list
#     print(num ** 2)


# 2. Use while loop
# 2.1 When you need to create an infinite loop

# while True:
#     game()

# 2.2 When you don't know the exact number of iterations beforehand, and want to continue until
# 2.2.1   ... the specific condition is no longer true

# import time

# counter = 5
# while counter > 0:
#     print(counter)
#     time.sleep(1)
#     counter -= 1
# print('blastoff!')

# 2.2.2  ... a break statement is encountered

# while True:
#     password = input('Please enter your password: ')
#     if password == '123456':
#         print('You are logged in. Welcome!')
#         break
#     else:
#         print('Try one more time!')
