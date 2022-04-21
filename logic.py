class wordlogic:
    def __init__(self):
        nothing = ''
        
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
        self.wordlist = sorteddict.keys()

    def guess(self, l1, l2, l3, l4, l5):
        listlist = [l1, l2, l3, l4, l5]
        for word in self.wordlist:
            for i in range(5):
                if word[i] not in listlist[i]:
                    self.wordlist.remove(word)
                
                

    def specify(self, i1, i1c, i2, i2c, i3, i3c, i4, i4c, i5, i5c, l1, l2, l3, l4, l5):
        
        alphalist = [l1, l2, l3, l4, l5]
        ilist = [i1, i2, i3, i4, i5]
        iclist = [i1c, i2c, i3c, i4c, i5c]

        for i in range(5):
            if iclist[i] == 'g':
                for letter in alphalist[i]:
                    if letter != ilist[i]:
                        alphalist[i].remove(letter)
            if iclist[i] == 'n':
                for l in alphalist:
                    l.remove(ilist[i])
            if iclist[i] == 'y':
                alphalist[i].remove(ilist[i])

        self.newlist1 = l1
        self.newlist2 = l2
        self.newlist3 = l3
        self.newlist4 = l4
        self.newlist5 = l5


            


        
        

        
        
        
            

    

       
            
            
        

       

        

        













