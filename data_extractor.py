import deck
import player
import pandas as pd

# create deck and player
d = deck.Deck()
pl = player.Player()


class mem:
    count = 0
    aces = 0
    value = 0
    result = 0
    save_value = 0
    cards = 0


def give_player_card_and_count():
    card = d.take_card()
    value = card.value
    mem.value += value
    mem.cards += 1
    if value > 9:
        mem.count -= 1
    if value < 7:
        mem.count += 1
    if value == 11:
        mem.aces += 1
    pl.give_card(card)

df = pd.DataFrame(columns = ["Count", "Aces" ,"Cards", "Value" , "Result"] )
# df = pd.read_csv("file1.csv", index_col=0)


data_entries = 0
while data_entries < 100000:
    if data_entries % 100 == 0:
        print(data_entries)
    give_player_card_and_count()
    give_player_card_and_count()
    while mem.value < 22:
        mem.result = 0
        mem.save_value = mem.value
        give_player_card_and_count()
        if mem.value < 22 and mem.value >= mem.save_value:
            mem.result = 1
        if mem.value < 22 and mem.value < mem.save_value:
            mem.result = 0.5
        df.loc[len(df)] =([mem.count, mem.aces, mem.cards, mem.save_value , mem.result ])
        data_entries += 1
        if d.cards_left() < 20:
            d = deck.Deck()
            mem.count = 0
    mem.value = 0
    mem.aces = 0
    mem.result = 0
    mem.cards = 0
    pl.init_or_reset_hand()





df.to_csv("file1.csv")
    


