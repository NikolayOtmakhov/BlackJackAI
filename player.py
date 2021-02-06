import pandas as pd

class Person(object):

    def __init__(self, name: str) -> None:
        self.cards = pd.DataFrame()
        self.name = name
        self.init_or_reset_hand()

    def init_or_reset_hand(self) -> None:
        self.cards = pd.DataFrame(index=['Main_Hand','Split_Hand'], columns=range(0,21))

    def cards_in_hand(self, Main_or_Split_Hand = "Main_Hand") -> None:
        return self.cards.count(axis=1)[Main_or_Split_Hand]

    def give_card(self, card, Main_or_Split_Hand = "Main_Hand") -> None:
        self.cards.at[str(Main_or_Split_Hand),self.cards_in_hand(Main_or_Split_Hand)] = card

    def card_value_total(self, Main_or_Split_Hand = "Main_Hand") -> None:
        number_of_aces = 0
        total_value = 0
        for i in range(0,self.cards_in_hand(Main_or_Split_Hand)):
            card_value = self.cards.loc[Main_or_Split_Hand][i].value
            if card_value == 11:
                number_of_aces += 1
            total_value += card_value
        for _ in range(number_of_aces):
            if total_value > 21:
                total_value -= 10
        return total_value

    def get_card_in_position(self, position: int, Main_or_Split_Hand: str = "Main_Hand") -> None:
        self.cards.loc[Main_or_Split_Hand][position]


class Player(Person):
 

    def __init__(self, name = "Human"):
        super().__init__(name)     
        self.round_status = pd.DataFrame(index=['Main_Hand','Split_Hand'], columns=["Status"])
        self.round_status.Status = ["Playing","NA"] 
        self.cash = 1000  

    def init_or_reset_hand(self):
        super().init_or_reset_hand()
        self.round_status = pd.DataFrame(index=['Main_Hand','Split_Hand'], columns=["Status"])
        self.round_status.Status = ["Playing","NA"]  

    def check_if_split(self):
        if self.cards_in_hand("Split_Hand") > 0:
            return True
        else:
            return False

    def get_round_status(self,Main_or_Split_Hand: str = "Main_Hand") -> str:
        return self.round_status.at[Main_or_Split_Hand,"Status"]


class Dealer(Person):

    def __init__(self, name: str):
        Person.__init__(self,name)
        self.bust = False