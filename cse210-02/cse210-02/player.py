from deck import Deck

class Player:
    '''comments'''
    def __init__(self):
        pass


    '''Method comments'''
    def start_game(self):
        pass

    '''Method comments'''
    def get_inputs(self):
        pass


    '''Method compares the users guess with the last number and updates score.'''
    def do_updates(self):
        # If keep_playing is false return
        if not self.keep_playing:
            return

        # Get correct answer
        if(self.point < self.last_point):
            self.answer = "l"
        elif(self.point > self.last_point):
            self.answer = "h"
        
        # Update score value
        if(self.guess == self.answer):
            self.score += 100
        else:
            self.score -= 75

        # Set last_point for next round
        self.last_point = self.point
        pass


    '''Method comments'''
    def do_outputs(self):
        pass


    
