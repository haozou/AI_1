'''
Created on 2013-1-26

the program is based on python 2.6

it is to simulate the tic_tac_toe game,

which is is a classic two-player turn-based 

game in which players try to get three Xs or

Os in a row on a 3x3 board.

there are two characters in this program,

one is the player, the other is the AI.

The starting player is selected randomly

@author: Hao Zou
'''

import random
# the chessboard
from player.player import cb
# the player
from player.player import Player
# the computer(AI)
from player.player import AI

# it is the player, use the "o" to represent him
player = Player("o")
# it is the computer, use the "x" to represent it
ai = AI("x")
# put the two character--player and AI to the tuple
# used to randomly select the starting player
character = (player,ai)
# used to output the message
cstring = ("player","AI")

# the run function, it is the main logic of this game,
# the player and the AI are playing one by one, the starting
# player is selected randomly.
def run():
    print "welcome to the tic_tac_toe"
    print "**********************"
    
    input = raw_input("are you ready? 1.yes 0.no\n")
    
    while input == "1":
        
        # show the chess board
        cb.clean_board()
        cb.show_board()
        
        # randomly choose the starting player
        i = random.randint(0,1)
        # output who is the starting player, the player or the AI
        print cstring[i],"first"
        
        # the two players play the gome one by one
        while 1:
            
            if character[i].play() == 1:
                break
            
            if character[(not i)].play() == 1:
                break
            
        input = raw_input("are you going to play again? 1.yes 0.no\n")
        if input == '0':
            break    
    print "bye"
    
if __name__ == '__main__':
    run()