from operator import contains
from os import umask
import random as rd

AH,AD,AC,AS = 1,1,1,1
H2,D2,C2,S2 = 2,2,2,2
H3,D3,C3,S3 = 3,3,3,3
H4,D4,C4,S4 = 4,4,4,4
H5,D5,C5,S5 = 5,5,5,5
H6,D6,C6,S6 = 6,6,6,6
H7,D7,C7,S7 = 7,7,7,7
H8,D8,C8,S8 = 8,8,8,8
H9,D9,C9,S9 = 9,9,9,9
H10,D10,C10,S10 = 10,10,10,10
JH,JD,JC,JS = 10,10,10,10
QH,QD,QC,QS = 10,10,10,10
KH,KD,KC,KS = 10,10,10,10

#Hemos usado 5 barajas de BlackJack
desk = [AH,AD,AC,AS,
        H2,D2,C2,S2,
        H3,D3,C3,S3,
        H4,D4,C4,S4,
        H5,D5,C5,S5,
        H6,D6,C6,S6,
        H7,D7,C7,S7,
        H8,D8,C8,S8,
        H9,D9,C9,S9,
        H10,D10,C10,S10,
        JH,JD,JC,JS,
        QH,QD,QC,QS,
        KH,KD,KC,KS,AH,AD,AC,AS,
        H2,D2,C2,S2,
        H3,D3,C3,S3,
        H4,D4,C4,S4,
        H5,D5,C5,S5,
        H6,D6,C6,S6,
        H7,D7,C7,S7,
        H8,D8,C8,S8,
        H9,D9,C9,S9,
        H10,D10,C10,S10,
        JH,JD,JC,JS,
        QH,QD,QC,QS,
        KH,KD,KC,KS,AH,AD,AC,AS,
        H2,D2,C2,S2,
        H3,D3,C3,S3,
        H4,D4,C4,S4,
        H5,D5,C5,S5,
        H6,D6,C6,S6,
        H7,D7,C7,S7,
        H8,D8,C8,S8,
        H9,D9,C9,S9,
        H10,D10,C10,S10,
        JH,JD,JC,JS,
        QH,QD,QC,QS,
        KH,KD,KC,KS,AH,AD,AC,AS,
        H2,D2,C2,S2,
        H3,D3,C3,S3,
        H4,D4,C4,S4,
        H5,D5,C5,S5,
        H6,D6,C6,S6,
        H7,D7,C7,S7,
        H8,D8,C8,S8,
        H9,D9,C9,S9,
        H10,D10,C10,S10,
        JH,JD,JC,JS,
        QH,QD,QC,QS,
        KH,KD,KC,KS,AH,AD,AC,AS,
        H2,D2,C2,S2,
        H3,D3,C3,S3,
        H4,D4,C4,S4,
        H5,D5,C5,S5,
        H6,D6,C6,S6,
        H7,D7,C7,S7,
        H8,D8,C8,S8,
        H9,D9,C9,S9,
        H10,D10,C10,S10,
        JH,JD,JC,JS,
        QH,QD,QC,QS,
        KH,KD,KC,KS]

x = 0

def cards_draw():
    player1 = []
    dealer = []
    player1_card1 = rd.choice(desk)
    player1.append(player1_card1)
    desk.remove(player1_card1)

    dealer_card1 = rd.choice(desk)
    dealer.append(dealer_card1)
    desk.remove(dealer_card1)

    player1_card2 = rd.choice(desk)
    player1.append(player1_card2)
    desk.remove(player1_card2)

    dealer_card2 = rd.choice(desk)
    dealer.append(dealer_card2)
    desk.remove(dealer_card2)
    
    print(dealer)
    print("----------------------------")
    print(player1)
    print("--------------------")
     
    return dealer,player1

def choices():
    dealer_and_player = cards_draw()
    dealer = tuple(dealer_and_player[0])
    player = tuple(dealer_and_player[1])
    
    if player in {(10,1),(1,10)}:
        player = 21
    elif player in {(9,1),(1,9)}:
        player = 20
    elif player in {(8,1),(1,8)}:
        player = 19
    elif player in {(7,1),(1,7)}:
        player = 18
    elif player in {(6,1),(1,6)}:
        player = 17
    elif dealer != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
        player = sum(player)
        
    if dealer in {(10,1),(1,10)}:
        dealer = 21
    elif dealer in {(9,1),(1,9)}:
        dealer = 20
    elif dealer in {(8,1),(1,8)}:
        dealer = 19
    elif dealer in {(7,1),(1,7)}:
        dealer = 18
    elif dealer in {(6,1),(1,6)}:
        dealer = 17
    elif dealer != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
        dealer = sum(dealer)
    return dealer,player
