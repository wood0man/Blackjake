import Deck;
import Player;
import random
"""
this game is based around getting to the total of 21 or as close to 21 before the game ends
you as a player can hit( pull an extra card) or stand( not pull an extra card) and you must place a
bet at the begining of the round. if you win you get 1.5 times your bet added to your bank

"""
# class Game():
#     def __init__(self,player,bank,bet):
#         player=Player.Player(player, bank,bet);
deck=Deck.Deck()
#pop cards so the player won't get any dup cards when he pulls
poppedPlayerCards=[];
for i in range(0,2):
    poppedPlayerCards.append(deck.allCards.pop())
player=Player.Player("Duaa",poppedPlayerCards, 2000,100);

print("Hello. I'm the dealer of this game. Now I'll give you your cards");
poppedDealerCards=[];
for i in range(0,2):
    poppedDealerCards.append(deck.allCards.pop())
dealer=Player.Player("Dealer", deck.allCards[2:4], 2000, 150);
dealerCardsValue=0;
playerCardsValue=0;
turn=0
while dealerCardsValue<21 or playerCardsValue<21 or turn<2:
    #this variable is used to print the final message in the case noone got to 21
    finalCheck=True;
    
    
    
    print("Your cards are:");
    
    for i in player.deck:
        print(i);
    for card in player.deck:
        #to check if there's an ace in the players deck and make the player choose it's value
        if "Ace" in card.suite:
            print("You have an ace. do you want it to have 10 or 1 value?")
            if input("My choice is...")=="10":
                card.value=10
            else: card.value=1
        
    print("The value:")
   
    for i  in player.deck:
        playerCardsValue+= i.value
    print(playerCardsValue)
    
    if playerCardsValue>21 :
        print("you've bitten the dust , Kidoo lol")
        finalCheck=False
        break;
        
    print("Dealer: What's your move , Kiddo?")
    correctMove=False;
    while not correctMove:
        print("Note you could either hit (Pull a card) or stand (not pull a card)")
        playerMove=input("My move is ...")
        #the move that the player made
        if playerMove.capitalize()=="Hit":
            player.hit()
            correctMove=True
            if playerCardsValue>21 :
                print("Dealer: you've bitten the dust , Kidoo lol")
                finalCheck=False
                break;
        elif playerMove.capitalize()=="Stand":
            player.stand()
            correctMove=True
        
        else: 
            print("That is not a move.")
    
    
    
    
    
    print("Your cards are:");
    for i in player.deck:
        print(i);
    print("The value:")
    value=0;
    for i  in player.deck:
        value+= i.value
    print(value)
    playerCardsValue=value
    
    if playerCardsValue>21 :
        print("you've bitten the dust , Kidoo lol")
        finalCheck=False
        break;




    dealer.hit()
    print("Dealer cards are:");
    dealerCardsValue=0;
    for i in dealer.deck:
        print(i);
    for card in dealer.deck:
        #to check if there's an ace in the dealer deck and make the player choose it's value
        if "Ace" in card.suite:
            
            if random.randint(1, 2)==1:
                card.value=10
            else:
                card.value=1
    print("The value:")
    value=0;
    for i  in dealer.deck:
        value+= i.value
    print(value)
    dealerCardsValue=value
    if dealerCardsValue>21 :
        print("I've bitten the dust :(")
        finalCheck=False
        player.bank+=player.bet*1.5
        print(f"your bank now is {player.bank}")
        break;
    playerCardsValue=0;
    dealerCardsValue=0;
    turn +=1
if finalCheck:

    if dealerCardsValue>playerCardsValue and dealerCardsValue<21:
        print("You've bitten the dust, kiddo lol")
    else:print("I've bitten the dust :(")