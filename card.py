class Card():

    def get_card_value(self, rank):
        try:
            value = int(rank)
            return value
        except:
            if rank == "Jack" or rank == "Queen" or rank == "King":
                return 10
            elif rank == "Ace":
                return 11

    def get_card_count(self, value):
        if value > 9:
            return -1
        elif value < 7:
            return 1
        else:
            return 0
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.get_card_value(rank)
        self.count = self.get_card_count(self.value)
        self.name = str(rank + "_of_" + suit) 
        self.img_loc = str(r"data/cards/" + rank + "_of_" + suit + ".png")

class CardBack():
    def __init__(self):
        self.name = str("Card Back") 
        self.img_loc = str(r"data/cards/card_back_black.png")
