with open("valid_words.txt") as file:
    WORDS = []
    for word in file.readlines():
        word = word.strip()
        if len(word) == 5:
            WORDS.append(word)
    file.close()