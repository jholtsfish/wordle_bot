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

<<<<<<< HEAD

        #remove all words with reoccurring letters from wordlines
        w1 = ''
        w2 = ''
        w3 = ''
        w4 = ''
        w5 = ''
        wlist = [w1, w2, w3, w4, w5]
        for n in range(len(wordlines)):
            for letter in range(5):
                wlist[letter] = wordlines[n][letter]
            for letter in wlist:
                for i in wlist:
                    if letter == i:
                        print(wordlines[int(n)])
                        wordlines.remove(wordlines[n])

        #switch out values in letters dicts for the decimal chance of that letter being in that indice 
        for dict in dictlist:
            for letter in dict:
                dict[letter] = float(dict[letter]) / float(8525)
        
        wordlinesdict = {}
        for word in wordlines:
            wordlinesdict[word] = float(letters1[word[1]]) * float(letters2[word[2]]) * float(letters3[word[3]]) * float(letters4[word[4]]) * float(letters5[word[5]]) * 100

        for i in range(len(wordlines)):
            print(str(wordlines[i]), (wordlinesdict[worldlines[i]]))



            

                    
                
=======
        #sort that dictionary
        self.sortedwords = sorted(wordlinesdict.items(), key = lambda kv: kv[1])
        
    
    def guess(self, previousword, letter1color, letter2color, letter3color, letter4color, letter5color):
        #colors can be y(ellow), g(reen), n(ull, or grey)
        print('.')


        
        

        
        
        
            

    

       
>>>>>>> d7524ad9593afbc46d5b5b5ac6c7f553680c1ee1
            
            
        

       

        

        













