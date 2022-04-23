import random, time

class logic:
    None
    def __init__(self):
        None
    def FindLetter(letter, lst):
        return any(letter in word for word in lst)
    def NextWord(dictOfWords):
        '''
        So, I'm taking in a dict with five letters as keys, with their values as their color. I need to figure out the best word to choose next. 
        '''
        wordfile = open('5words.txt', 'r')
        wordlines = wordfile.readlines()
        for i in range(len(wordlines) -1, -1, -1):
            wordlines[i] = wordlines[i].strip()
            if len(wordlines[i]) != 5:
                wordlines.remove(wordlines[i])
        validWords = wordlines
        validWords1 = []
        badWords = []
        probWords = []
        guessedWords = []
        while True:        
            letters = {}
            letterPos = {}
            otherWords = []
            correctWord = []
            posBad = []
            inWord = []
            notInWord = []
            counter = 1
            for letter in dictOfWords:
                if dictOfWords[letter]   == 'green':
                    letters.update({letter: 'green'})
                    letterPos.update({letter: counter})
                    counter += 1
                    continue
                elif dictOfWords[letter] == 'yellow':
                    letters.update({letter: 'yellow'})
                    letterPos.update({letter: counter})
                    counter += 1
                    continue
                elif dictOfWords[letter] == 'gray':
                    letters.update({letter: 'gray'})
                    letterPos.update({letter: counter})
                    counter += 1
                    continue
            for letter in letters:
                if letters[letter] == 'green':
                    correctWord.append(letter)
                    continue
                elif letters[letter] == 'yellow':
                    inWord.append(letter)
                    continue
                elif letters[letter] == 'gray':
                    notInWord.append(letter)
                    continue
            for word in validWords:
                string = word
                for letter in word: 
                    if letter in notInWord:
                        badWords.append(word)
                        continue
            for word in validWords:
                for letter in inWord:
                    if letter not in word:
                        badWords.append(word)
                        continue
                    elif letter in word:
                        probWords.append(word)
                        continue
            validWords.clear()
            probWords = list(dict.fromkeys(probWords))
            badWords = list(dict.fromkeys(badWords))
            for word in probWords:
                if word not in badWords:
                    validWords.append(word)
                    continue
                elif word in badWords:
                    continue
            letterList = []
            validWords1.clear()
            true = True
            wordChoice = random.choice(validWords)
            length = len(inWord)
            print(wordChoice, len(validWords))
            more = iter(input('next set please:').split())
            dictOfWords.clear()
            dictOfWords.update(dict(zip(more, more)))
            print(validWords)
            continue
    NextWord({'a': 'gray', 'd': 'yellow', 'i': 'gary', 'e': 'yellow', 'u': 'gray'})
