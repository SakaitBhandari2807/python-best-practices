from random import shuffle

from Card import suits, ranks, Card


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def draw_one(self):
        return self.all_cards.pop()




