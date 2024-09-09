# import module_example


# print(module_example.x)


name = input("What is your name? >> ")

# if name == 'Zhi':
#     print(f'Hi, {name}!')
# else:
#     print('Get out of here, hacker!')


age = input("What is your age? ")
# print(type(age))

age = int(age)
print(type(age))

if name == "Zhi" or age >= 21:
    print("Yes, you can!")
else:
    print("No, you cannot!")
