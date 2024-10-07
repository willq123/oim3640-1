import webbrowser


def solve(url, word, replacement):
    """Create the new url and open it"""
    new_url = url.replace(word, replacement)
    webbrowser.open(new_url)


def main():
    url = "http://www.pythonchallenge.com/pc/def/0.html"
    res = str(2**38)

    solve(url, "0", res)


main()
