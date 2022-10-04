from deck import Card


'''Create Player class and start the game. The player has a few responsibilities. 
To start the game, keep score, make a card guess, and update score according to players choice. '''
class Player:
    
    def __init__(self):
        '''Create values for the player class to be initalized.'''
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
        # If keep_playing is false return
        if not self.playing:
            return
        # Repeated code from deck since I was unable to grab it
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        # Get new random card if the same card is drawn redraw
        card = Card()
        #new_card = card.point # Having a rough time getting this to return a new random value instead of old which creates infinite loop in while
        new_card = random.choice(list(card_values.keys())) # Temp solution
        if(new_card == self.card1):
            while(new_card == self.card1):
                card = Card()
                #new_card = card.point
                new_card = random.choice(list(card_values.keys()))

        # Get number card value
        card_one = card_values.get(self.card1)
        card_two = card_values.get(new_card)

        # Get correct answer
        if(card_two < card_one):
            answer = "l"
        elif(card_two > card_one):
            answer = "h"
        
        # Update score value
        if(self.guess == answer):
            self.score += 100
        else:
            self.score -= 75

        # Set the "new_card" as card1 for next round
        self.card1 = new_card
        pass

    '''Method comments'''

    def do_outputs(self):
        pass
