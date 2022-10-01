import random


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}


random_point = random.choice(list(card_values.keys()))
random_suit = random.choice(suits)


class Card:
    def __init__(self):
        self.point = random_point
        self.suit = random_suit
