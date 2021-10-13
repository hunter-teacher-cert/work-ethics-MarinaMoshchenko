import math
import random

class Player:
    def __init__(self, letter): #Mangling: python interpreter modifies variable name with ___, to avoid conflicts with subclasses.
        #letter either x or o
        self.letter = letter
        
    # we want all players to get their next move given in a game
    def get_move(self, game)
        pass
    
    class RandomComputerPlayer(Player):
        def __init__(self, letter):
            super()._init_(letter)
            
        def get_move(self, game):
            # get a random valid spot for our next move
            square = random.choice(game.available_moves())
            return square
        
    class HumanPlayer(Player):
        def __init__(self, letter):
            super()._init_(letter)
        
        def get_move(self, game):
            valid_square = False
            val = None
            while not valid_square:
                square = input(self.letter + '\'s turn. Input move (0-8):')
                # We will check if this is a correct value by trying to cast
                # in to an integer, and if it's not, then we say it's invalid
                # if that spot is not available on the board, we also say it's invalid
                try:
                    val = int(square)
                    if val not in game.available_moves():
                        raise ValueError
                    valid_square = True # if it is successful
                except ValueError:
                    print('Invalid square. Try again.")
            
            return val
            