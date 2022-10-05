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
        self.guess = ""


    def start_game(self):
            '''Starts the game by going throuhg all required methods in order to play. The order will be 
            Show card, Draw card, Player guess, update points, and repeat until player no longer wishes
            continue or player runs out of points.'''
            self.card1 = self.card.draw_card()

            while self.playing:
                self.get_inputs()
                self.do_updates()
                self.do_outputs()


    '''Method comments'''

    def get_inputs(self):
        pass

    '''Method comments'''

    def do_updates(self):
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
        if(new_card == self.card1):
            while(new_card == self.card1):
                card = Card()
                new_card = card.draw_card()

        # Get correct answer
        if(point2 < point1):
            answer = "l"
        elif(point2 > point1):
            answer = "h"
        
        # Update score value
        if(self.guess == answer):
            self.score += 100
        else:
            self.score -= 75

        # Set the "new_card" as card1 for next round
        self.card1 = {point2: suit2}

        # Check for end of game
        if(self.score == 0):
            userInput = input("Do you want to play again: [y/n]: ")
            if (userInput.lower == "y"):
                self.playing = True
            elif(userInput.lower == "n"):
                self.playing = False
        pass

    '''Method comments'''

    def do_outputs(self):
        pass
