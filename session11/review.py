# Get the middle character(s) in a string


def get_middle(s):
    """return the middle character(s) in a string"""
    if len(s) % 2 == 1:  # If the string contains odd number of characters
        return  # Get the middle one
    else:
        return  # Get the middle two


# print(get_middle('ABC'))  # B
# print(get_middle('ABCD'))  # BC


def contains_no_vowels(s):
    """
    Return True if s contains no vowels ('a', 'e', 'i', 'o', 'u'), otherwise return False

    Check every letter in the string:
        if the letter is a vowel:
            return False
    return True
    """
    for letter in s:
        if letter in "aeiouAEIOU":
            return False  # return will immediately end the function
        # else:
        #     return True    # return will immediately end the function
    return True


print(contains_no_vowels("abc"))  # False
print(contains_no_vowels("bbc"))  # True
print(contains_no_vowels("babson"))  # False


# Yesterday (20241001) is a perfect square number. Can you find the next one?


