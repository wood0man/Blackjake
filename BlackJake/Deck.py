import Cards


class Deck():
    
    allCards=[]
    for i in Cards.suite:
        for j in Cards.rank:
            card=Cards.Cards(i, j);
            allCards.append(card)    
    def __init__(self):
        pass
        