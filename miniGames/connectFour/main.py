'''
Author: Roberto Angel Tun
Date: 01/04/24
Description: creating a CLI connect four game
'''

# create a matrix to represent board with zeros (using numpy) board size = 6 x 7
# allow user to enter piece (only enter the column) make to switch user (current player)
# update board when piece is entered and if it is valid
# check if there is a winner

import numpy as np

board = np.zeros((6, 7))

def update_board(board, placement):
    column = board[:,(placement-1)] #acces to the column trying to update
    for row in reversed(range(len(column))): #iterating through the column
        if column[row] == 0: 
            column[row] = 2
    board[:, placement-1] = column
    print(board)

update_board(board, 4)