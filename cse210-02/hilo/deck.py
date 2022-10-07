import random

class Card:
    def __init__(self):
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self.card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        self.random_point = random.choice(list(self.card_values.keys()))
        self.random_suit = random.choice(self.suits)

        self.point = self.random_point
        self.suit = self.random_suit

    def draw_card(self):
        full_card = {self.point: self.suit}
        return full_card
