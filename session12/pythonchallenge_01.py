import webbrowser


def decrypt(s):
    """
    Return the message that is decrypted from original message, s
    """
    res = ""

    # Iterate ove each char in s:
    #     shift the char 2 places to right
    #     add it back to res
    for c in s:
        if c.isalpha():
            if c == "y":  # There must be a better/more elegant way, % 26
                res += "a"
            elif c == "z":
                res += "b"
            else:
                new_c = chr(ord(c) + 2)
                res += new_c
        else:
            res += c

    return res


def solve(url, word, replacement):
    """Create the new url and open it"""
    new_url = url.replace(word, replacement)
    webbrowser.open(new_url)


def main():
    url = "http://www.pythonchallenge.com/pc/def/map.html"
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    decrypted_message = decrypt(message)
    print(decrypted_message)

    decrypted_word = decrypt("map")
    solve(url, "map", decrypted_word)


main()
