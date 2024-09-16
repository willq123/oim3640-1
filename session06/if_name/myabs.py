def my_abs(number):
    """Return the absolute value of a number"""
    if number < 0:
        return -number
    else:
        return number


def main():
    print(my_abs(-10))  # some test code
    print(my_abs(30))
    print(__name__)


if __name__ == "__main__":
    # We don't want the main() to be executed when this module is imported in other file
    main()
