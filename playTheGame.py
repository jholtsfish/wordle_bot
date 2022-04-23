import collections
import random, time, enum

class logic:
    None
    def __init__(self):
        self.wordfile = open('5words.txt', 'r')
        self.wordlines = self.wordfile.readlines()
        for i in range(len(self.wordlines) -1, -1, -1):
            self.wordlines[i] = self.wordlines[i].strip()
            if len(self.wordlines[i]) != 5:
                self.wordlines.remove(self.wordlines[i])
        self.validWords = self.wordlines
        self.validWords1 = self.wordlines
        self.badWords = []
        self.choiceList = []
    def NextWord(self, dictOfWords, validWords = None):
        if validWords is None:
            validWords = self.validWords
        letters = []
        gLetters = []
        words = ''
        for letter in dictOfWords:
            words += letter
            if dictOfWords[letter] == 'green':
                letters.append('green')
                continue
            elif dictOfWords[letter] == 'yellow':
                letters.append('yellow')
                continue
            elif dictOfWords[letter] == 'gray':
                letters.append('gray')
                continue
        for word in validWords:
            for letter in range(len(letters)):
                if letters[letter] == 'green' and words[letter] != word[letter]:
                    self.badWords.append(word)
                    gLetters.append(word[letter])
                    break
                elif letters[letter] == 'yellow' and (words[letter] not in word or words[letter] == word[letter]):
                    self.badWords.append(word)
                    gLetters.append(word[letter])
                    break
                elif letters[letter] == 'gray' and words[letter] in word:
                    self.badWords.append(word)
                    break
                '''
            if not all(letter in word for letter in greenLetters):
                print('green letters that arent in the word', letter, word, greenLetters)
                time.sleep(5)
                '''
        validWords1 = validWords
        validWords = []
        for word in validWords1:
            if word in self.badWords:
                continue
            elif word not in self.badWords:
                validWords.append(word)
        choice = random.choice(validWords)
        self.choiceList += choice
        while True:
            if choice in self.choiceList:
                 choice = random.choice(validWords)
                 continue
            else:
                break
        return choice