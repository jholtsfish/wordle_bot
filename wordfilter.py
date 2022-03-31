#this file just filters out all of the non 5 letter words from a wordlist 

wordlist = '400k4lines.txt'

wordfile = open(wordlist, 'r')
wordlines = wordfile.readlines()

for i in range(len(wordlines) -1, -1, -1):
            wordlines[i] = wordlines[i].strip()
            if len(wordlines[i]) != 5:
                print(f"removing word: {wordlines[i]}")
                wordlines.remove(wordlines[i])

wordfile.close()
with open('200k5words.txt', 'w') as f:
    f.writelines("%s\n" % l for l in wordlines)

