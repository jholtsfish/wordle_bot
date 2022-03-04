class valid_words:
    valid_words = None
    invalid_words = None
    untested_words = None
    def __init__(self):
        self.untested_words = []
        while True:
            with open('valid_words.txt', 'r') as data:
                lines = data.readlines()
            True