# Build our own bit.ly service (URL shortening)
# www.babson.edu -> bit.ly/3AadHr9 (some random chars)
# www.google.com -> bit.ly/4880vj6

import string
import random


random.seed(42)

long_2_short = {}  # e.g. {'www.babson.edu': '3AadHr9'}
short_2_long = {}  # {'3AadHr9': 'www.babson.edu'}


def shorten(url, n=7):
    """
    Convert the long url to a shorter url, and return it

    url: original url to shorten
    n: the length of the shortened url
    """
    if url in long_2_short:  # Check if the short url was generated before
        return long_2_short[url]
    else:  # if the short url was not generated before
        availables = string.ascii_letters + string.digits
        short = "".join(random.choices(availables, k=n))
        # Assume this short is unique
        # Store the URL: short to the dict url_2_short
        long_2_short[url] = short
        short_2_long[short] = url
        return short


# def convert_back(short):
#     """Convert the short URL back to original
#     """

original = "www.babson.edu"
short_url = shorten(original)


print(f"{original}: bit.ly/{short_url}")
print(short_2_long[short_url])
