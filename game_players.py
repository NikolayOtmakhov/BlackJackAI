import player
import file_manager

class Players:

    def get_nb_players(self):
        return file_manager.Json("game_settings").read("number_of_players")
    
    def add_player_to_game(self):
        self.players.append(player.Player())

    # give all player the first card before the second card
    def deal_cards(self, deck):
        self.mem.done_dealing = False
        for desired_cards_in_hand in range(1,3):
            for player in self.players:
                if player.cards_in_hand() < desired_cards_in_hand:
                    card = deck.take_card()
                    self.mem.count += card.count
                    player.give_card(card)
            if self.dealer.cards_in_hand() < desired_cards_in_hand:
                card = deck.take_card()
                if self.dealer.cards_in_hand() == 0:
                    self.mem.dealer_hidden_card_count += card.count
                else:
                    self.mem.count += card.count
                self.dealer.give_card(card)
        self.mem.done_dealing = True    

    def __init__(self, deck, memory):
        self.mem = memory
        self.dealer = player.Dealer("Dealer Man")
        self.players = []
        for _ in range(self.get_nb_players()):
            self.add_player_to_game()
        self.deal_cards(deck)
    
