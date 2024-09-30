# Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack
prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    # if letter == "O" or letter == "Q":
    if letter in 'OQ':
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
