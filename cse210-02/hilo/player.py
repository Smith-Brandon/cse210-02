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
        '''Starts the game by going through all required methods in order to play. The order will be 
        draw_card, get_guess, do_updates, do_outputs, continue_playing, and repeat until player no longer wishes
        continue or player runs out of points.'''
        print()
        print("Welcome to Hi-Lo! A card game testing your luck.")
        print("The game is simple.  You will be shown a card")
        print("and you must guess whether the next card will")
        print("be higher(h) or lower(l) if you guess correctly")
        print("you earn 100 points but if you guess incorrectly")
        print("you will lose 75 points.  You can play as long ")
        print("as you would like but if you reach 0 the game")
        print("ends.  Good luck and have fun!")
        print()
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

        self.guess = None

        while self.guess != "h" and self.guess != "l":
            self.guess = input("Higher or lower? [h/l] ").lower()
            if self.guess != "h" and self.guess != "l":
                print("That is not a valid input. Please enter a valid input.")

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

        # Check if the new card has the same value as the old card
        if (point1 == point2):
            while (new_card == self.card1):
                card = Card()
                new_card = card.draw_card()
                point2 = list(new_card.keys())[0]

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
        if (self.score <= 0):
            print("You lost!")
            self.playing = False
        pass

    def continue_playing(self):
        """Asks the user if they want to continue playing

        Args:
            self (Player): An instance of the player
        """
        if self.playing == False:
            new_game = None
            while new_game != "y" and new_game != "n":
                new_game = input(
                    "Would you like to start a new game? [y/n] ").lower()
                if new_game == "y":
                    self.restart_game()
                elif new_game == "n":
                    quit()
                else:
                    print("Invalid input. Please enter a valid input.")
        else:
            cont_game = None
            while cont_game != "y" and cont_game != "n":
                cont_game = input(
                    "Do you want to continue the game? [y/n] ").lower()
                if cont_game == "y":
                    self.playing = True
                elif cont_game == "n":
                    self.playing = False
                else:
                    print("Invalid input. Please enter a valid input.")
            print("\n")

    def restart_game(self):
        """Resets all values to their initial state

        Args:
            self (Player): An instance of the player
        """
        self.playing = True
        self.score = 300
        self.card = Card()
        self.card1 = 0
        self.new_card = 0
        self.guess = ""
        self.start_game()

    def do_outputs(self):
        """Prints the what the next card and the score after the updated score
        Args: 
            self (Player): An instance of the player
        """
        # If statement ends the game when the player hits zero
        if self.playing == False:
            pass
        else:
            point = list(self.card1.keys())[0]
            suit = list(self.card1.values())[0]
            print(f"Next card was: {point} of {suit}")

            print(f"Your score is: {self.score}")
            pass
