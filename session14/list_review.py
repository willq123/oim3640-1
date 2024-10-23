s1 = "cameron"
s2 = "romance"


def is_anagram(a: str, b: str):
    """
    Return True if a an b are anagrams
    """
    print(sorted(a))
    print(sorted(b))
    return sorted(a) == sorted(b)


# print(is_anagram(s1, s2))
# print(is_anagram('stop', 'pots'))


def remove_even(numbers):
    """
    Return a list of numbers after removing all the even integers
    """
    # You CANNOT modify the list while iterating over the same list

    # for i, n in enumerate(numbers):
    #     print(i, n)
    #     if n % 2 == 0:
    #         print(f' removing {n}')
    #         numbers.remove(n)  # Wrong
    # return numbers

    # Correct way: Create a new empty list, only appending non-even items from the original list

    # res = []
    # for n in numbers:
    #     if n % 2 == 0:
    #         continue
    #     else:
    #         res.append(n)
    # return res

    res = numbers[:]
    for n in numbers:
        if n % 2 == 0:
            res.remove(n)
    return res


s = [11111, 222222, 33333, 444, 44, 5555, 6666]
print(remove_even(s))
