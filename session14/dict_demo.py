def histogram(s):
    d = {} # initialize the dict for counting
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        # print(d)
        # d[c] = d.get(c, 0) + 1
    return d

counter = histogram("bookkeeper")
print(counter)
# print('b' in counter)



# Solve Python Challenge Puzzle #2

file = open('data/pythonchallenge_2.txt')
s = file.read()
res = histogram(s)
print(res)



# Only print the chars that appear once in the 
for k, v in res.items():
    if v == 1:
        print(k)