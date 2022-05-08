from wordlogic import wordlogic
from weblogic import webinterface

wordlogic = wordlogic()

webinterface = webinterface()

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

glist1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
glist2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
glist3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
glist4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
glist5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

for i in range(500):
    print("\n")


answerlist = wordlogic.sortwords('12words.txt')
guesslist = wordlogic.sortwords('2words.txt')

#(self, i1, i1c, i2, i2c, i3, i3c, i4, i4c, i5, i5c, l1, l2, l3, l4, l5) is the pattern for wordlogic.specify

#use cares as starting word for round 1

gameround = int(1)

webinterface.enterword(wordlogic.nextword)

webinterface.reapdata(gameround)

wordlogic.eliminate_answers(wordlogic.nextword, webinterface.lettercolors[0], webinterface.lettercolors[1], webinterface.lettercolors[2], webinterface.lettercolors[3], webinterface.lettercolors[4], list1, list2, list3, list4, list5, answerlist)

wordlogic.eliminate_guesses(wordlogic.nextword, webinterface.lettercolors[0], webinterface.lettercolors[1], webinterface.lettercolors[2], webinterface.lettercolors[3], webinterface.lettercolors[4], glist1, glist2, glist3, glist4, glist5, guesslist)

gameround += 1

for i in range(5):
        webinterface.enterword(wordlogic.nextword)

        webinterface.reapdata(gameround)

        wordlogic.eliminate_answers(wordlogic.nextword, webinterface.lettercolors[0], webinterface.lettercolors[1], webinterface.lettercolors[2], webinterface.lettercolors[3], webinterface.lettercolors[4], list1, list2, list3, list4, list5, answerlist)

        wordlogic.eliminate_guesses(wordlogic.nextword, webinterface.lettercolors[0], webinterface.lettercolors[1], webinterface.lettercolors[2], webinterface.lettercolors[3], webinterface.lettercolors[4], glist1, glist2, glist3, glist4, glist5, guesslist)

        gameround += 1
        if webinterface.youwin == True:
                print('YOU WIN!')
                break
