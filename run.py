from logic import wordlogic

wordlogic = wordlogic()

#lists for eliminating words in wordlogic

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

wordfile = input("use custom wordlist? [default: none] --> ")
if '.' not in wordfile:
    wordfile = '2words.txt'
wordlogic.sortwords(wordfile)

#(self, i1, i1c, i2, i2c, i3, i3c, i4, i4c, i5, i5c, l1, l2, l3, l4, l5) is the pattern for wordlogic.specify

#use cares as starting word for round 1
for i in range(5):
    wordlogic.specify(str(input('\nindex 1: -->')), str(input('\nindex 1 color: --> ')), str(input('\nindex 2: --> ')), str(input('\nindex 2 color: --> ')), str(input('\nindex 3: --> ')), str(input('\nindex 3 color: --> ')), str(input('\nindex 4: --> ')), str(input('\nindex 4 color: --> ')), str(input('\nindex 5: --> ')), str(input('\nindex 5 color: --> ')), list1, list2, list3, list4, list5)

    wordlogic.guess(wordlogic.newlist1, wordlogic.newlist2, wordlogic.newlist3, wordlogic.newlist4, wordlogic.newlist5)