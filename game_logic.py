import deck
import game_players
import player
import dealer_logic

class BlackJack:

    def reset(self):
        self.game_deck = deck.Deck()
        self.players = game_players.Players(self.game_deck, self.mem)
        self.player_turn = 0
        self.round_finished = False
        self.done_dealing = False
        self.dealer_card_hidden = True
        self.text = ["test", "test"]

    def get_current_player(self):
        if self.player_turn < len(self.players.players):
            return self.players.players[self.player_turn]
        else: 
            return self.players.dealer

    def __init__(self, memory):
        self.mem = memory
        self.reset()


    # test main and split hand on every button action for loss if playing
    # if both not playing sets current player to next player
    # also check for dealier turn 
    def update_player_status(self):
        # check not dealer
        if self.player_turn != len(self.players.players):
            # main hand
            if self.get_current_player().round_status.at['Main_Hand',"Status"] == "Playing":
                if self.get_current_player().card_value_total('Main_Hand') > 21:
                    self.get_current_player().round_status.at['Main_Hand',"Status"] = "Lost"
            # split hand
            elif self.get_current_player().round_status.at['Split_Hand',"Status"] == "Playing":
                if self.get_current_player().card_value_total('Split_Hand') > 21:
                    self.get_current_player().round_status.at['Split_Hand',"Status"] = "Lost"
            # next player
            if self.get_current_player().round_status.at['Main_Hand',"Status"] != "Playing" and self.get_current_player().round_status.at['Split_Hand',"Status"] != "Playing":
                self.player_turn += 1
        # check if dealer
        if self.player_turn == len(self.players.players):
            dealer_logic.RoundEnd(self.mem, self)

    #after round ends - continue button
    def reset_round(self):
        #reset platers and dealers 
        for player in self.players.players:
            player.init_or_reset_hand()
        self.players.dealer.init_or_reset_hand()
        
        # reset game values
        self.player_turn = 0
        self.done_dealing = False
        self.round_finished = False

        # deal new cards
        self.players.deal_cards(self.game_deck)