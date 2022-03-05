with open("valid_words.txt") as file:
    WORDS = [word for word in (word.strip() for word in file.readlines()) if len(word) == 5]
    file.close()

print(WORDS)