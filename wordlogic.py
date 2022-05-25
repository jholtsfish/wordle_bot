class wordlogic:
    def __init__(self):
        self.nextword = 'cares'
        self.useguesses = False

    def filterwords(self, unfilteredfile, writefile):
        with open(unfilteredfile, 'r') as wordfile:

            wordlines = wordfile.readlines()

            for i in range(len(wordlines) -1, -1, -1):
                        wordlines[i] = wordlines[i].strip()
                        if len(wordlines[i]) != 5:
                            print(f"removing word: {wordlines[i]}")
                            wordlines.remove(wordlines[i])

        with open(writefile, 'w') as f:
            f.writelines("%s\n" % l for l in wordlines)

    def sortwords(self, filepath):
        #read the txt file containing words, remove all non 5 letter words and then put them in a list
        wordfile = open(filepath, 'r')
        wordlines = wordfile.readlines()
        for i in range(len(wordlines) -1, -1, -1):
            wordlines[i] = wordlines[i].strip()
            if len(wordlines[i]) != 5:
                wordlines.remove(wordlines[i])

        #dicts for each index in the 5 letter word, keys are the letters of the alphabet, values are how many times the letter was found in the dicts index. (changed to a new value later)
        letters1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        letters2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        letters3 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        letters4 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        letters5 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        dictlist = [letters1, letters2, letters3, letters4, letters5]
        wordlinesdict = {}

        #adding +1 to the value of letters every time they are found in a certain index in a word
        for line in wordlines:
            letters1[line[0]] += 1
            letters2[line[1]] += 1
            letters3[line[2]] += 1
            letters4[line[3]] += 1
            letters5[line[4]] += 1
        
        #convert dict values from how many times a letter appears, to the % of the time that it appears (%chance that the letter will appear)
        for dict in dictlist:
            for letter in dict:
                dict[letter] = float(dict[letter]) / float(12653)

        #add every word to a dictionary, then assign a value to it based on the %chance for each letter that i just did above
        for word in wordlines:
            wordlinesdict[word] = float(letters1[word[0]]) * float(letters2[word[1]]) * float(letters3[word[2]]) * float(letters4[word[3]]) * float(letters5[word[4]]) * 100000000

        #sort that dictionary
        sorteddict = ({key: value for key, value in sorted(wordlinesdict.items(), key=lambda item: item[1])})
        wordlist = list(sorteddict.keys())
        return (wordlist)

    def eliminate_answers(self, word, i1c, i2c, i3c, i4c, i5c, l1, l2, l3, l4, l5, wordlist):
        letterlist = []
        for letter in word:
            letterlist.append(letter)

        colorlist = [i1c, i2c, i3c, i4c, i5c]

        possiblelist = [l1, l2, l3, l4, l5]

        rmlist = []

        for i in range(5):
            #what to do with a green letter
            if colorlist[i] == 'g':
                possiblelist[i] = ['g']
            for word in wordlist:
                if letterlist[i] not in word and word not in rmlist:
                    rmlist.append(word)
            #what to do with a yellow letter
            if colorlist[i] == 'y':
                if letterlist[i] in possiblelist[i]:
                    possiblelist[i].remove(letterlist[i])
                for word in wordlist:
                    if letterlist[i] in word and word not in rmlist:
                        rmlist.append(word)
            #what to do with a gray (n) letter
            if colorlist[i] == 'n':
                for possibility in possiblelist:
                    if letterlist[i] in possibility:
                        possibility.remove(letterlist[i])

        for word in wordlist:
            for i in range(5):
                if word[i] not in possiblelist[i] and word not in rmlist:
                    rmlist.append(word)

        for word in rmlist:
            wordlist.remove(word)

        if len(wordlist) == 0:
            self.useguesses = True
        else:
            self.nextword = str(wordlist[-1])
            self.useguesses = False


    def eliminate_guesses(self, word, i1c, i2c, i3c, i4c, i5c, l1, l2, l3, l4, l5, wordlist):
        letterlist = []
        for letter in word:
            letterlist.append(letter)

        colorlist = [i1c, i2c, i3c, i4c, i5c]

        possiblelist = [l1, l2, l3, l4, l5]

        rmlist = []

        for i in range(5):
            #what to do with a green letter
            if colorlist[i] == 'g':
                for possibility in possiblelist:
                    if letterlist[i] in possibility:
                        possibility.remove(letterlist[i])
                for word in wordlist:
                    if letterlist[i] in word and letterlist[i] not in rmlist:
                        rmlist.append(word)
            #what to do with a yellow letter
            if colorlist[i] == 'y':
                if letterlist[i] in possiblelist[i]:
                    possiblelist[i].remove(letterlist[i])
                for word in wordlist:
                    if letterlist[i] not in word and word not in rmlist:
                        rmlist.append(word)
            #what to do with a gray (n) letter
            if colorlist[i] == 'n':
                for possibility in possiblelist:
                    if letterlist[i] in possibility:
                        possibility.remove(letterlist[i])
                for word in wordlist:
                    if letterlist[i] in word and word not in rmlist:
                        rmlist.append(word)

        for word in wordlist:
            for i in range(5):
                if word[i] not in possiblelist[i] and word not in rmlist:
                    rmlist.append(word)

        for word in rmlist:
            wordlist.remove(word)

        if self.useguesses == True:
            self.nextword = wordlist[-1]
