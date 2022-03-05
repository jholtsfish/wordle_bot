class wordlogic:
    def __init__(self):
        good = 'good'
    def sortwords(self, filepath):
        wordfile = open(filepath, 'r')
        wordlines = wordfile.readlines()
        for line in wordlines:
            line.strip()
            print(line)





