from login import Login

thing = Login()

with open("valid_words.txt") as file:
    # words = file.readlines()
    # words = [word.strip() for word in words]
    words = [word for word in (word.strip() for word in file.readlines()) if len(word) == 5]

    file.close()

print(words)
print(thing)