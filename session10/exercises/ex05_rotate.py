def rotate(word, n):
    """
    Take a string, WORD, and an integer, N as parameters,
    return a new string that contains the letters from the original
    string, WORD, rotated by the given amount, N.
    """
    s = ""
    for c in word:
        if c.isalpha():
            if c.islower():
                shift = (ord(c) - ord("a") + n) % 26
                s += chr(ord("a") + shift)
            else:
                shift = (ord(c) - ord("A") + n) % 26
                s += chr(ord("A") + shift)
        else:
            s += c
    return s


def main():
    print(rotate("abc", 2))
    print(rotate("xyz", 2))
    print(rotate("0-9, A-Z", 2))


if __name__ == "__main__":
    main()
