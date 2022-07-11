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


def dealer_and_player1_draw():
        #Hemos usado 5 barajas de BlackJack
        deck = [AH,AD,AC,AS,
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


        player1 = []
        dealer = []
        player1_card1 = rd.choice(deck)
        player1.append(player1_card1)
        deck.remove(player1_card1)

        dealer_card1 = rd.choice(deck)
        dealer.append(dealer_card1)
        deck.remove(dealer_card1)

        player1_card2 = rd.choice(deck)
        player1.append(player1_card2)
        deck.remove(player1_card2)

        dealer_card2 = rd.choice(deck)
        dealer.append(dealer_card2)
        deck.remove(dealer_card2)
        
        return dealer,player1,deck

def first_playing_method(): #El jugador se queda con las dos cartas principales; WINRATE = 38.6 %
    dealer_and_player = dealer_and_player1_draw()
    dealer = tuple(dealer_and_player[0])
    player = tuple(dealer_and_player[1])
    deck = dealer_and_player[2]
    
    
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
    elif player != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
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
    
    while dealer < 17:
        new_dealer_card = rd.choice(deck)
        deck.remove(new_dealer_card)
        dealer = (dealer,new_dealer_card)
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
    
    if dealer > 21:
        win_lose_tie = 1        #player win = 1 ; player loose/tie = 0
    elif dealer > player:
        win_lose_tie = 0
    elif dealer == player:
        win_lose_tie = 0
    else :
        win_lose_tie = 1
           
                  
    return int(win_lose_tie)

def second_playing_method(): #El jugador juega como el dealer; WINRATE = 40,8 %
    dealer_and_player = dealer_and_player1_draw()
    dealer = tuple(dealer_and_player[0])
    player = tuple(dealer_and_player[1])
    deck = dealer_and_player[2]
    
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
    elif player != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
        player = sum(player)
    
    while player < 17:
        new_player_card = rd.choice(deck)
        deck.remove(new_player_card)
        player = (player,new_player_card)
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
        elif player != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
            player = sum(player)
    
    if player > 21:
        win_lose_tie = 0 
    else:
        
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
        
        while dealer < 17:
            new_dealer_card = rd.choice(deck)
            deck.remove(new_dealer_card)
            dealer = (dealer,new_dealer_card)
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
        
        if dealer > 21:
            win_lose_tie = 1        #player win = 1 ; player loose/tie = 0
        elif dealer > player:
            win_lose_tie = 0
        elif dealer == player:
            win_lose_tie = 0
        else :
            win_lose_tie = 1
            
                  
    return int(win_lose_tie)

def third_playing_method(): #El jugador juega como el dealer;WINRATE = 38.5 % (7 o mas) ;WINRATE = 38,6 % (8 o mas); WINRATE = 38.85 % (9 o mas); WINRATE = 39,5 % (10 o mas) ;WINRATE = 40,5 % (11 o mas) ; WINRATE = 42,2 % (12 o mas); WINRATE = 42.44 % (13 o mas) ;WINRATE = 42,417 % (14 o mas); WINRATE = 42,1 % (15 o mas) ;WINRATE = 41,5 % (16 o mas) ; WINRATE = 40,7 % (17 o mas) ;WINRATE = 39,4 % ( 18 o más) ; WINRATE = 35,482 % (19 O MAS) ; WINRATE = 28,4 % (20 o mas); WINRATE = 15 % (21)
    dealer_and_player = dealer_and_player1_draw()
    dealer = tuple(dealer_and_player[0])
    player = tuple(dealer_and_player[1])
    deck = dealer_and_player[2]
    
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
    elif player != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
        player = sum(player)
    
    while player < 14: #Aqui sustituyes en qué numero quieres quedarte;
        new_player_card = rd.choice(deck)
        deck.remove(new_player_card)
        player = (player,new_player_card)
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
        elif player != {(10,1),(1,10), (9,1),(1,9),(8,1),(1,8),(7,1),(1,7),(6,1),(1,6)}:
            player = sum(player)
    
    if player > 21:
        win_lose_tie = 0 
    else:
        
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
        
        while dealer < 17:
            new_dealer_card = rd.choice(deck)
            deck.remove(new_dealer_card)
            dealer = (dealer,new_dealer_card)
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
        
        if dealer > 21:
            win_lose_tie = 1        #player win = 1 ; player loose/tie = 0
        elif dealer > player:
            win_lose_tie = 0
        elif dealer == player:
            win_lose_tie = 0
        else :
            win_lose_tie = 1
            
                  
    return int(win_lose_tie)


player_winrate = []

while len(player_winrate) < 10000001: #sample of one million
    player_winrate.append(third_playing_method())

player_winrate = sum(player_winrate)

print(" The winner rate is: ", player_winrate/100000, "%" )


#El jugador juega como el dealer;WINRATE = 38.5 % (7 o mas) ;WINRATE = 38,6 % (8 o mas); 
# WINRATE = 38.85 % (9 o mas); WINRATE = 39,5 % (10 o mas) ;WINRATE = 40,5 % (11 o mas) ; 
# WINRATE = 42,2 % (12 o mas); WINRATE = 42.44 % (13 o mas) ;WINRATE = 42,417 % (14 o mas); 
# WINRATE = 42,1 % (15 o mas) ;WINRATE = 41,5 % (16 o mas) ; WINRATE = 40,7 % (17 o mas) ;
# WINRATE = 39,4 % ( 18 o más) ; WINRATE = 35,482 % (19 O MAS) ; WINRATE = 28,4 % (20 o mas); 
# WINRATE = 15 % (21)
