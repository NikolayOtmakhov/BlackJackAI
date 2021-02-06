class RoundEnd:
    def __init__(self, mem, game):
        self.game = game
        game.dealer_card_hidden = False
        mem.count += mem.dealer_hidden_card_count
        mem.dealer_hidden_card_count = 0
        while game.players.dealer.card_value_total() < 17:
            card = self.game.game_deck.take_card()
            mem.count += card.count
            game.players.dealer.give_card(card)
        self.check_for_winners()
        
    def check_for_winners(self):
        self.game.text = []
        dealer_count = self.game.players.dealer.card_value_total()
        for count, player in enumerate(self.game.players.players):
            if player.card_value_total() > dealer_count and player.card_value_total() < 22:
                player.cash += 100
                self.game.text.append(f"Player {count + 1} Won! - Cash: {player.cash}")
                print(f"Player {count + 1} Won! - Cash: {player.cash}")
            elif player.card_value_total() == dealer_count and player.card_value_total() < 22:
                self.game.text.append(f"Player {count + 1} Tie  - Cash: {player.cash}")
                print(f"Player {count + 1} Tie  - Cash: {player.cash}")

            else:
                player.cash -= 100
                self.game.text.append(f"Player {count + 1} Lost - Cash: {player.cash}")
                print(f"Player {count + 1} Lost - Cash: {player.cash}")
            if player.round_status.at['Split_Hand',"Status"] != "NA":
                if player.card_value_total("Split_Hand") > dealer_count and player.card_value_total("Split_Hand") < 22:
                    player.cash += 100
                    self.game.text.append(f"Player {count + 1} Split Hand Won! - Cash: {player.cash}")
                    print(f"Player {count + 1} Split Hand Won! - Cash: {player.cash}")
                elif player.card_value_total("Split_Hand") == dealer_count and player.card_value_total("Split_Hand") < 22:
                    self.game.text.append(f"Player {count + 1} Split Hand Tie  - Cash: {player.cash}")
                    print(f"Player {count + 1} Split Hand Tie  - Cash: {player.cash}")

                else:
                    player.cash -= 100
                    print(f"Player {count + 1} Split Hand Lost - Cash: {player.cash}")

        print("-------------------------------------------------------------")
        self.game.round_finished = True
        