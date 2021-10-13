import time
from Player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self): # Double underscore, Mangling - python interpreter modifies variable name with ___. To avoid conflicts with subclasses
        self.board = [' ' for _ in range(9)] #single list to represent 3x3 board
        self.current_winner = None #to keep track of winner
        
    def print_board(self):
        # to get the rows
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' '] #the same as lines 50-55 in comments
        
    def empty_squares(self):
        return len(self.available_moves())
    
    def num_empty_squares(self):
        return self.board.count(' ') #len(self.available_moves())
    
    def make_move(self, square, letter):
        # if move is valid, make the move (assign square to letter)
        # then return True. If invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row, check the following conditions
        # CHECK ROW:
        row_ind = square // 3 #floor division
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # CHECK COLUMN:
        col_ind = square % 3
        column = [self.board[col_ind+1*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # CHECK DIAGONALS
        # Only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left ro right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
            
        # if all these conditions fail
        return False
        

def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game (letter), or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # we return the winner
    #that breaks the loop
    while game.empty_squares():
        # get the move from the appropriate player
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # define a function to make a move - line 27-33
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print.board()
                print('') # empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
              
              #after the move we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' #switches player, same as in lines below
        
        #tiny break to make it easier to read
            time.sleep(0.8)
        
        if print_game:
            print('It\'s a tie!')
            
    if __name__ == '_main_':
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game = True)
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#               return[i for i, spot in enumerate(self.board) if spot == ' '] #the same as lines 50-55 in comments   
# SAME AS ------------------------------------------------------------------------------
#             moves = []
#             for (i, spot) in enumerate(self.board):
#                 #['x', 'x', 'o']
#                 if spot == ' ':
#                     moves.append(i)
#                 return moves




#             letter = 'O' if letter == 'X' else 'X' #switches player, same as in lines
# SAME AS:------------------------------------------------------------------------------
#             if letter == 'X':
#                 letter = 'O'
#             else:
#                 letter = 'X'

        