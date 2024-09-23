# score = 95


def check_score(score):
    if score >= 60:
        print("Pass")
        return  # `return` will immediately end the function
    if score >= 90:
        print("A")
    else:
        print("Fail")


# score = 55
# check_score(score)


def f(a, b, c=0):
    # return a * 10 + b
    return a * 100 + b * 10 + c


print(f(2, 3, 1))  # positional arguments

print(f(b=3, a=2, c=1))  # keyword arguments

print(f(2, 3))  # c is using the default value


def f1(a, b):
    print(a + b)


def f2():
    """
    Uses f1() to print a + b. No return
    """
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    f1(a, b)


# print(f2())
f2()

