'''
Created on 2013-1-26

this file contains the Class Player and

the Class AI, AI inherits the Player.

@author: Hao Zou
'''
import time
from chessboard.chessboard import ChessBoard

# the chess board
cb = ChessBoard(3,3)

# the class Player, used to implement the player's behavior
class Player:
    # initial function, used to initialize the representative 
    # of the player, if it is the AI, use "x", if it is the
    # player, use "o"
    def __init__(self,name):
        self.name = name
    # the play function for the player, the main logic for the
    # player's behavior
    def play(self):
        print "it is your turn"
        while 1:
            row = raw_input("row:")
            column = raw_input("column:")
            # if the input is not legal, should re-input
            if (not row.isdigit()) or (not column.isdigit()):
                print "please input the number"
                continue
            
            flag = self.step(int(row), int(column)) 
            # if the player's position is not legal, should re-input
            # the position
            if flag == -1:
                continue
            else:
                break
        # if the chess board is full, should exit the game
        if cb.isfull() == 1:
            print "it is tie"
            return 1
        # if the player is win, should exit the game
        if cb.is_win("o") == 1:
            print "you win"
            return 1
    # the player's next step
    def step(self,row,column):
        if row > cb.row or column > cb.column:
            print "error position"
            return -1
        if not cb.board[row-1][column-1] == 0:
            print "position has been taken"
            return -1
        cb.change_board(row, column, self.name)
        cb.show_board()
        
# the class AI, used to implement the AI's behavior
# inherit the Class Player        
class AI(Player):
    # overload the play function
    def play(self):
        print "waiting for the AI"
        time.sleep(1)
        
        # find all the possible position for the AI
        poses = self.search_empty_blank()
        # find the best position in all these possible position
        best_pos = self.get_best_pos(poses)
        
        # update the chess board
        row = best_pos[0]+1
        column = best_pos[1]+1
        cb.change_board(row,column , self.name)
        cb.show_board()

        # it is the same as the play function in the class Player
        if cb.isfull() == 1:
            print "it is tie"
            return 1
        if cb.is_win("x") == 1:
            print "AI wins"
            return 1
        
    # return the best position for the AI
    def get_best_pos(self, poses):
        # if it is the first step for the AI,
        # it should take the center of the chess board
        if len(poses) >= 8:
            for pos in poses:
                if pos == (1,1): 
                    return pos

        max = 0
        min = 0
        best_pos_max = (1,1)
        best_pos_min = (1,1)
        # get both the best position for the AI and the player
        for pos in poses:
            score = self.get_max_score(pos)
            #print pos, score
            if score > max:
                max = score
                best_pos_max = pos
            score = self.get_min_score(pos)
            #print pos, score
            if score < min:
                min = score
                best_pos_min = pos
        # if the score of the best pos for the AI is bigger than the
        # absolute value of the score of the best pos for the player, 
        # that mean we should choose the former one, otherwise we 
        # choose the latter one.
        if max >= -min:
            best_pos = best_pos_max
        else:
            best_pos = best_pos_min
        
        return best_pos
    # find the empty blank in the chess board for the AI
    def search_empty_blank(self):
        poses = []
        for i in range(cb.row):
            for j in range(cb.column):
                if cb.board[i][j] == 0:
                    poses.append((i,j))
        return poses
    # get the max score for each empty blank in the chess board
    # for the AI; the blank with the max score means it is the best
    # blank for the AI
    def get_max_score(self,pos):
        score = 0
        count = 0
        # compute the score for the row
        for i in range(cb.row):
            if i == pos[0]:
                for j in range(cb.column):
                    if cb.board[i][j] == "x":
                        count += 1
                    if cb.board[i][j] == "o":
                        count -= 1
        if count <= 0:
            score += 0
        elif count == 1:
            score += 20
        elif count == 2:
            score += 100
        
        count = 0    
        # compute the score for the column
        for j in range(cb.column):
            if j == pos[1]:
                for i in range(cb.row):
                    if cb.board[i][j] == "x":
                        count += 1
                    if cb.board[i][j] == "o":
                        count -= 1
        if count <= 0:
            score += 0
        elif count == 1:
            score += 20
        elif count == 2:
            score += 100    
            
        count = 0
        i = 0
        j = 0
        # compute the score for the diagonal
        if pos[0] == pos[1]:
            while i < cb.row and j < cb.column:
                if cb.board[i][j] == "x":
                    count += 1
                if cb.board[i][j] == "o":
                    count -= 1
                i += 1
                j += 1
            if count <= 0:
                score += 0
            elif count == 1:
                score += 20
            elif count == 2:
                score += 100
            
        count = 0
        i = 0
        j = cb.row - 1
        
        if pos[0] + pos[1] == 2:        
            while i < cb.row and j >= 0:
                if cb.board[i][j] == "x":
                    count += 1
                if cb.board[i][j] == "o":
                    count -= 1
                i += 1
                j -= 1
            if count <= 0:
                score += 0
            elif count == 1:
                score += 20
            elif count == 2:
                score += 100   
                
        return score
    # get the min score for each empty blank in the chess board
    # for the AI; the blank with the min score means it is the best
    # blank for the player.
    def get_min_score(self,pos):
        score = 0
        count = 0
        # compute the score for the row
        for i in range(cb.row):
            if i == pos[0]:
                for j in range(cb.column):
                    if cb.board[i][j] == "o":
                        count += 1
                    if cb.board[i][j] == "x":
                        count -= 1
        if count <= 0:
            score -= 0
        elif count == 1:
            score -= 20
        elif count == 2:
            score -= 100
        
        count = 0    
        # compute the score for the column
        for j in range(cb.column):
            if j == pos[1]:
                for i in range(cb.row):
                    if cb.board[i][j] == "o":
                        count += 1
                    if cb.board[i][j] == "x":
                        count -= 1
        if count <= 0:
            score -= 0
        elif count == 1:
            score -= 20
        elif count == 2:
            score -= 100  
            
        count = 0
        i = 0
        j = 0
        # compute the score for the diagonal
        if pos[0] == pos[1]:
            while i < cb.row and j < cb.column:
                if cb.board[i][j] == "o":
                    count += 1
                if cb.board[i][j] == "x":
                    count -= 1
                i += 1
                j += 1
            if count <= 0:
                score -= 0
            elif count == 1:
                score -= 20
            elif count == 2:
                score -= 100
            
        count = 0
        i = 0
        j = cb.row - 1
        
        if pos[0] + pos[1] == 2:        
            while i < cb.row and j >= 0:
                if cb.board[i][j] == "o":
                    count += 1
                if cb.board[i][j] == "x":
                    count -= 1
                i += 1
                j -= 1
            if count <= 0:
                score -= 0
            elif count == 1:
                score -= 20
            elif count == 2:
                score -= 100  
                
        return score