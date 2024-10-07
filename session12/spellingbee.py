# https://www.nytimes.com/puzzles/spelling-bee


def at_least(word, n):
    """Return True if the word has at least n letters"""
    # if len(word) >= n:
    #     return True
    # else:
    #     return False
    return len(word) >= n


def must_include(word, letter):
    """Return True if the word contains the required letter"""
    return letter in word


def use_only(word, available):
    """
    Return True if the word uses only the available letters, return False if any letter in word is not from the available letters
    """
    # check each letter in word
    #   if letter is not from the available letters:
    #       return False
    # After checking all the letters in word:
    # return True
    for letter in word:
        if letter not in available:
            return False
    return True


# print(use_only("babson", "abcd"))  # False
# print(use_only("babson", "absonxyz"))  # True


def solve(must_have, available):
    """Solve spellingbee puzzle
    print all the qualified words
    """
    f = open("data/words.txt")  # open the word list file

    # Iterate over the word list, check each word
    #   if the word is qualified (at least 4 letters, must include the must_have letter, use only the available letters)
    #        print the word

    for line in f:
        # print(line, len(line))
        word = line.strip()  # Get each word after removing the ending '\n'
        if (
            at_least(word, 4)
            and must_include(word, must_have)
            and use_only(word, available)
        ):
            print(word)


def main():
    # what information?
    center_letter = "m"
    other_letters = "acgeko"

    solve(center_letter, other_letters)  # with the information


main()
