from playTheGame import logic
l = logic()
word = {}
for i in range(5):
    more = iter(input('next set please:').split())
    word.clear()
    word.update(dict(zip(more, more)))
    print(l.NextWord(word))