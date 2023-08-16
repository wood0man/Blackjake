import Deck;
import Player;
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

print("Hello. I'm the dealer of this game. Now i'll give you your cards");
poppedDealerCards=[];
for i in range(0,2):
    poppedDealerCards.append(deck.allCards.pop())
dealer=Player.Player("Dealer", deck.allCards[2:4], 2000, 150);
dealerCardsValue=0;
playerCardsValue=0;
    
while dealerCardsValue<21 or playerCardsValue<21:
    print("Your cards are:");
    
    for i in player.deck:
        print(i);
    print("The value:")
   
    for i  in player.deck:
        playerCardsValue+= i.value
    print(playerCardsValue)
    
    if playerCardsValue>21 :
        print("you've bitten the dust , Kidoo lol")
        break;
        
    print("Dealer: What's your move , Kiddo?")
    
    if input("My move is...").capitalize()=="Hit":
        player.hit()
        if playerCardsValue>21 :
            print("Dealer: you've bitten the dust , Kidoo lol")
            break;
    elif input("My move is...").capitalize()=="Stand":
        player.stand()
    
    
    
    
    
    
    
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
        break;




    dealer.hit()
    print("Dealer cards are:");
    dealerCardsValue=0;
    for i in dealer.deck:
        print(i);
    print("The value:")
    value=0;
    for i  in player.deck:
        value+= i.value
    print(value)
    dealerCardsValue=value
    if dealerCardsValue>21 :
        print("I've bitten the dust ,:(")
        break;
