'''
Created on 2013-1-26

This is the Class ChessBoard

it is used to define the behavior of

the chess board

@author: Hao Zou
'''

class ChessBoard:

    # initial function. we use two-dimensional array to represent the chess board
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.board = [([0] * row) for i in range(column)]
    # change the value of the given position in the array
    def change_board(self,row,column,value):
        self.board[row-1][column-1] = value
    # judge whether the player is winning the game
    def is_win(self,name):
        # if the player is taking all the same row
        count = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j] == name:
                    count += 1
                j += 1
            if count == self.column:
                return 1
            else:
                count = 0
            j = 0
            i += 1
        # if the player is taking all the same column
        count = 0     
        for j in range(self.column):
            for i in range(self.row):
                if self.board[i][j] == name:
                    count += 1
                i += 1
            if count == self.row:
                return 1
            else:
                count = 0
            i = 0
            j += 1
        # if the player is taking all the same slash
        i = 0
        j = 0
        count = 0
        while i < self.row and j < self.column:
            if self.board[i][j] == name:
                count += 1
            i += 1
            j += 1
    
        if count == self.row:
            return 1

        
        # if the player is taking all the same anti-slash
        i = 0
        j = self.row - 1
        count = 0
        while i < self.row and j >= 0:
            if self.board[i][j] == name:
                count += 1
            i += 1
            j -= 1
        if count == self.row:
            return 1
    # judge whether the chess board is full
    def isfull(self):
        count = 0
        for row in self.board:
            for column in row:
                if column == 0:
                    count += 1 
        if count == 0:
            return 1
    # clean the chess board
    def clean_board(self):
        self.board = [([0] * self.row) for i in range(self.column)]
        
    # show the chess board
    def show_board(self):
        print "**********************"
        for row in self.board:
            for column in row:
                print column,
            print 
        print "**********************"    
        
if __name__ == '__main__':
    #test use
    cb = ChessBoard(3,3)
    cb.change_board(1, 1, '*')
    cb.change_board(2, 1, 'o')
    cb.change_board(2, 2, 'o')
    cb.change_board(2, 3, 'o')
    cb.is_win("o")
    cb.show_board()