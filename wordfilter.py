#this file just filters out all of the non 5 letter words from a wordlist 

wordlist = 'put the path to your wordlist here'

wordfile = open(wordlist, 'r')
wordlines = wordfile.readlines()

for i in range(len(wordlines) -1, -1, -1):
            wordlines[i] = wordlines[i].strip()
            if len(wordlines[i]) != 5:
                wordlines.remove(wordlines[i])