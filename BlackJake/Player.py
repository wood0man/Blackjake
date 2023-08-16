import random
import Deck

gameDeck=Deck.Deck();
#make the game deck
random.shuffle(gameDeck.allCards);

class Player():
    def __init__(self,name,deck,bank,bet):
        #bank is the amount of money the player has in his bank
        self.playerDeck=[];
        self.name=name;
        self.bank=bank;
        self.bet=bet
        self.deck=deck
        

    
    
    
    #take an extra card    
    def hit(self):
        if len(gameDeck.allCards)==0:
            print("I don't have any cards to give to you")
            return
        self.deck.append(gameDeck.allCards[0])
    #don't take an extra card
    def stand(self):
        print("{self.name} says: I'm satistfied with my cards")