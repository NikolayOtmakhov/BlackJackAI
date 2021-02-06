import game_cards
import game_background
import game_buttons
import numpy as np

class Functions:
    def __init__(self,memory, game):
        self.mem = memory
        self.game = game
        
    def _check_hand(self):
        if self.game.get_current_player().round_status.at['Main_Hand',"Status"] == "Playing":
            return "Main_Hand"
        else:
            return "Split_Hand"

    def hit(self):
        if self.mem.done_dealing:
            if self.game.player_turn < len(self.game.players.players):
                # give card and add to count
                card = self.game.game_deck.take_card()
                self.mem.count += card.count
                self.game.get_current_player().give_card(card, self._check_hand())
                # end action
                self.game.update_player_status()

    def stand(self):
        if self.mem.done_dealing:
            if self.game.player_turn < len(self.game.players.players):
                self.game.get_current_player().round_status.at[self._check_hand(),"Status"] = "Stand"
                # end action
                self.game.update_player_status()

    def double_down(self):
        if self.mem.done_dealing:
            if self.game.player_turn < len(self.game.players.players):
                if self.game.get_current_player().round_status.at['Main_Hand',"Status"] == "Playing":
                    if self.game.get_current_player().cards_in_hand() == 2:
                        self.hit()
                        # Hit would jump to nex player if over 21 - so only if its under 21 jump to next
                        if self.game.get_current_player().card_value_total("Main_Hand") <= 21 and not self.game.get_current_player().cards_in_hand() == 2:
                            self.stand()
                else:
                    if self.game.get_current_player().cards_in_hand("Split_Hand") == 2:
                        self.hit()
                        if self.game.get_current_player().card_value_total("Split_Hand") <= 21:
                            self.stand()
    
    def split(self):
        if self.mem.done_dealing:
            if self.game.player_turn < len(self.game.players.players):
                try:
                    if self.game.get_current_player().cards_in_hand("Split_Hand")==0:
                        if self.game.get_current_player().cards.loc["Main_Hand"][0].rank == self.game.get_current_player().cards.loc["Main_Hand"][1].rank:
                            # Move players second card to split deck
                            self.game.get_current_player().cards.at[str("Split_Hand"),0] = self.game.get_current_player().cards.at[str("Main_Hand"),1]
                            self.game.get_current_player().cards.at[str("Main_Hand"),1] = np.NaN
                            # Give card to main and split hand and add to count
                            for hand in ["Main_Hand","Split_Hand"]:
                                card = self.game.game_deck.take_card()
                                self.mem.count += card.count
                                self.game.get_current_player().give_card(card,hand)  
                            # Change status of split hand from NaN
                            self.game.get_current_player().round_status.at['Split_Hand',"Status"] = "Playing"  
                except:
                    pass


    def next_round(self):
        if self.game.round_finished == True:
            self.game.reset_round()
            self.game.dealer_card_hidden = True
    
