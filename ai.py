import tensorflow.keras as keras
import numpy as np


class AI:
    def __init__(self, memory, game, functions):
        self.mem = memory
        self.blackjack_model = \
            keras.models.load_model('saved_model/blackjack_model')
        self.game = game
        self.functions = functions
        
    def action(self):
        if self.game.player_turn < len(self.game.players.players):
            aces = 0
            for card in self.game.get_current_player().cards.loc["Main_Hand"].dropna():
                if card.rank == "Ace":
                    aces += 1
            cards = self.game.get_current_player().cards_in_hand()
            value = self.game.get_current_player().card_value_total()
            hit_certainty = \
                self.blackjack_model.predict(
                    [[self.mem.count #count
                    ,aces
                    ,cards
                    ,value]])[0][0]
            if hit_certainty > 0.45:
                self.functions.hit()
            else:
                self.functions.stand()
