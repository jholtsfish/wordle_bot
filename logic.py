class wordlogic:
    def __init__(self):
        gkjdfsksdfkjgsd = 'yo'
    def sortwords(self, filepath):
        wordfile = open(filepath, 'r')
        wordlines = wordfile.readlines()
        for i in range(len(wordlines) -1, -1, -1):
            wordlines[i] = wordlines[i].strip()
            if len(wordlines[i]) != 5:
                wordlines.remove(wordlines[i])
        letters1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        letters2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        letters3 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        letters4 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        letters5 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0 , 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        optimword = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        for line in wordlines:
            letters1[line[0]] += 1
            letters2[line[1]] += 1
            letters3[line[2]] += 1
            letters4[line[3]] += 1
            letters5[line[4]] += 1
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        for i in letters1:
            l1.append(letters1[i])
        for i in letters2:
            l2.append(letters2[i])
        for i in letters3:
            l3.append(letters3[i])
        for i in letters4:
            l4.append(letters4[i])
        for i in letters5:
            l5.append(letters5[i])
        l1 = sorted(l1)
        l2 = sorted(l2)
        l3 = sorted(l3)
        l4 = sorted(l4)
        l5 = sorted(l5)
        let1best = 1
        let1top = 'a'
        dict1sum = 0
        dict2sum = 0 
        dict3sum = 0 
        dict4sum = 0 
        dict5sum = 0

        sumlist = [dict1sum, dict2sum, dict3sum, dict4sum, dict5sum]
        dictlist = [letters1, letters2, letters3, letters4, letters5]


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



            

                    
                
            
            
        

       

        

        













