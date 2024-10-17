def count(word, letter):
    """Return how many times the character, LETTER, appears in WORD"""
    counter = 0
    for ch in word:
        if ch == letter:
            counter = counter + 1
    return counter


def main():
    print(count("New England Patriots", "a"))


if __name__ == "__main__":
    main()
