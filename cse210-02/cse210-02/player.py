from deck import Deck

'''Create Player class and start the game. The player has a few responsibilities. 
To start the game, keep score, make a card guess, and update score according to players choice. '''
class Player:
    '''Create values for the player class to be initalized.'''
    def __init__(self):
        self.playing = True
        self.score = 300


    def start_game(self):
            '''Starts the game by going throuhg all required methods in order to play. The order will be 
            Show card, Draw card, Player guess, update points, and repeat until player no longer wishes
            continue or player runs out of points.'''
            card1 = self.draw_card()

            while self.is_playing:

                self.get_inputs()
                self.do_updates()
                self.do_outputs()


    '''Method comments'''
    def get_inputs(self):
        pass


    '''Method comments'''
    def do_updates(self):
        pass


    '''Method comments'''
    def do_outputs(self):
        pass


    
