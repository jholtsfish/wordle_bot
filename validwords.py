class valid_words:
    valid_words = None
    invalid_words = None
    untested_words = None
    def __init__(self):
        self.untested_words = []
        with open('valid_words.txt', 'r') as data:
            lines = data.readlines()
            for line in data.readlines():
                line.split()