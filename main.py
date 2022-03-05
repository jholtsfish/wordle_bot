from login import Login
from init import WORDS

thing = Login()

with open("valid_words.txt") as file:
    words = [word for word in (word.strip() for word in file.readlines()) if len(word) == 5]
    file.close()