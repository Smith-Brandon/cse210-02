from sys import setdlopenflags
from deck import Card


'''Create Player class and start the game. The player has a few responsibilities. 
To start the game, keep score, make a card guess, and update score according to players choice. '''


class Player:

    def __init__(self):
        '''Create values for the player class to be initalized.'''
        self.playing = True
        self.score = 300
        self.card = Card()
        self.card1 = 0
        self.new_card = 0
        self.guess = ""

    def start_game(self):
        '''Starts the game by going throuhg all required methods in order to play. The order will be 
        Show card, Draw card, Player guess, update points, and repeat until player no longer wishes
        continue or player runs out of points.'''
        self.card1 = self.card.draw_card()

        while self.playing:
            self.get_guess()
            self.do_updates()
            self.do_outputs()
            self.continue_playing()

    def get_guess(self):
        """Asks the user if they think the next card is higher or lower

        Args:
            self (Player): An instance of the player
        """
        point = list(self.card1.keys())[0]
        suit = list(self.card1.values())[0]
        print(f"The card is {point} of {suit}")

        self.guess = input("Higher or lower? [h/l] ")

    def do_updates(self):
        answer = ""
        # If keep_playing is false return
        if not self.playing:
            return
        # Card1 values
        point1 = list(self.card1.keys())[0]
        suit1 = list(self.card1.values())[0]

        # Get new random card if the same card is drawn redraw
        card = Card()
        new_card = card.draw_card()

        # Card2 values
        point2 = list(new_card.keys())[0]
        suit2 = list(new_card.values())[0]

        # Check if the same card was drawn
        if (new_card == self.card1):
            while (new_card == self.card1):
                card = Card()
                new_card = card.draw_card()

        # Get correct answer
        if (point2 < point1):
            answer = "l"
        elif (point2 > point1):
            answer = "h"

        # Update score value
        if (self.guess == answer):
            self.score += 100
        else:
            self.score -= 75

        # Set the "new_card" as card1 for next round
        self.card1 = {point2: suit2}

        # Check for end of game
        if (self.score == 0):
            print("You lost!")
        pass

    def continue_playing(self):
        """Asks the user if they want to continue playing

        Args:
            self (Player): An instance of the player
        """
        cont_game = input("Do you want to continue the game? [y/n] ")
        if cont_game == "y":
            self.playing = True
        elif cont_game == "n":
            self.playing = False
        print("\n")


    def do_outputs(self):
        point = list(self.card1.keys())[0]
        suit = list(self.card1.values())[0]
        print(f"Next card was: {point} of {suit}")

        print(f"Your score is: {self.score}")
        pass
