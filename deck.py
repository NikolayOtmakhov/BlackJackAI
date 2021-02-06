import card
import random
import file_manager

class Deck():
    suits = ["Hearts","Diamonds","Spades","Clubs"]
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def get_nb_decks(self):
        if self.nb_decks == None:
            return file_manager.Json("game_settings").read("number_of_decks")
        else:
            return self.nb_decks

    def create_new_game_deck(self):
        self.game_deck = []
        for _ in range(self.get_nb_decks()):
            for suit in self.suits:
                for rank in self.ranks:
                    self.game_deck.append(card.Card(rank,suit))
        random.shuffle(self.game_deck)

    def __init__(self,nb_decks=None):
        self.nb_decks = nb_decks
        self.create_new_game_deck()
        

    def reset_deck(self, decks):
        self.create_new_game_deck()

    def take_card(self):
        return self.game_deck.pop()

    def show_cards(self):
        for card in self.game_deck:
            print(card.name)
    
    def cards_left(self):
        return len(self.game_deck)