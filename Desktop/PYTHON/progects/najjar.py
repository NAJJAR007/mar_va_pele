#bazi mar va pele
import random
p_1 = 0
p_2 = 0
#first problem
while 1:
    if p_1 == 6:
        break
    else:
        while p_1 != 6:
            X = input("press enter for roll")
            p_1 = random. randint(1, 6)
            print(f"dice p_1: {p_1}")
            if p_1 != 6:
                print("try again p_1")
#OR
    while 1:
        p_2 = random. randint(1, 6)
        print(f"dice p_2: {p_2}")
        if p_2 == 6:
            break
        else:
            print("try again p_2")
'''
#zamin 50 khanehee
tedad_khane = range(0 , 51)
zamin = [x for x in tedad_khane]
'''
if p_1 == 6:
    p_1 == 1
if p_2 == 6:
    p_2 == 1

p_1L = 0
p_2L = 0

#first problem
while 1:
#p_2 loop
    while 1:
        if p_1 == 50 and p_2 == 50:
            print("DRAW!")
            exit()
        if p_2 < 50 :
            print(f"p_2 is {p_2}")
        if p_2 > 50 :
            p_2 = p_2 - p_2L
            print(f"p_2 is {p_2}")
            print("--> player 2 must try again")

        if p_2 == 50 :
            #print(f"p_1 is {p_1}")
            print(f"p_2 is {p_2}")
            print("p_2 WIN!")
            exit()
        p_2L = random. randint(1, 6)
        print(f"dice p_2: {p_2L}")
        p_2 = p_2 + p_2L
#p_1 loop
    while 1:
        if p_1 == 50 and p_2 == 50:
            print("DRAW!")
            exit()
        if p_1 < 50 :
            print(f"p_1 is {p_1}")
        if p_1 > 50 :
            p_1 = p_1 - p_1L
            print(f"p_1 is {p_1}")
            print("--> player 1 must try again")
        if p_1 == 50 :
            print(f"p_1 is {p_1}")
            #print(f"p_2 is {p_2}")
            print("p_1 WIN!")
            exit()

        X = input("press enter for roll")
        p_1L = random. randint(1, 6)
        print(f"dice p_1: {p_1L}")
        p_1 = p_1 + p_1L
'''
first problem
    loopi ke age yeki 6 omad va break shod on yeki to loop bemone
    ta vaghti dar biyad
second problem
    p_1: 6
    p_2: 5
    ________
    p_1: 6
    p_2: 0
    ________
    p_1: 3
    p_2: 0
    p_1 is 15
    p_2 is 5
third problem
    sakhtan marha va peleha
'''