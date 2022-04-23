#file to run stuff in logic.py

from logic import wordlogic

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
list5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

wordlogic = wordlogic()

wordlogic.sortwords('2words.txt')

print(wordlogic.wordlist)

#(self, i1, i1c, i2, i2c, i3, i3c, i4, i4c, i5, i5c, l1, l2, l3, l4, l5)
wordlogic.specify(str(input('i1')), str(input('i1c')), str(input('i2')), str(input('i2c')), str(input('i3')), str(input('i3c')), str(input('i4')), str(input('i4c')), str(input('i5')), str(input('i5c')), list1, list2, list3, list4, list5)

wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.specify(str(input('i1')), str(input('i1c')), str(input('i2')), str(input('i2c')), str(input('i3')), str(input('i3c')), str(input('i4')), str(input('i4c')), str(input('i5')), str(input('i5c')), wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.specify(str(input('i1')), str(input('i1c')), str(input('i2')), str(input('i2c')), str(input('i3')), str(input('i3c')), str(input('i4')), str(input('i4c')), str(input('i5')), str(input('i5c')), wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.specify(str(input('i1')), str(input('i1c')), str(input('i2')), str(input('i2c')), str(input('i3')), str(input('i3c')), str(input('i4')), str(input('i4c')), str(input('i5')), str(input('i5c')), wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)
            
wordlogic.specify(str(input('i1')), str(input('i1c')), str(input('i2')), str(input('i2c')), str(input('i3')), str(input('i3c')), str(input('i4')), str(input('i4c')), str(input('i5')), str(input('i5c')), wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)

wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)
