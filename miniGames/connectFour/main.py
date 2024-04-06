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

def update_board(board, placement, currentPlayer):
    rowUsed = 0
    column = board[:,(placement-1)] #acces to the column trying to update
    for row in reversed(range(len(column))): #iterating through the column
        if column[row] == 0: 
            column[row] = currentPlayer
            rowUsed = row
            break
    board[:, placement-1] = column
    return board, rowUsed

def checkWinner(board, currentPlayer):
    # checking for horizontal wins
    for row in range(len(board)):
        for column in range(4):
            if (board[row][column] == currentPlayer and board[row][column+1]== currentPlayer and board[row][column+2]== currentPlayer and board[row][column+3]== currentPlayer):
                return "Winner"
    # checking for vertical wins
    for row in range(len(board)):
        for column in range(4):
            if (board[row][column] == currentPlayer and board[row+1][column]== currentPlayer and board[row+2][column]== currentPlayer and board[row+3][column]== currentPlayer):
                return "Winner"
    # checking for diagonal wins
    for row in range(len(board)-3):
        for column in range(3, 7):
            if (board[row][column] == currentPlayer and board[row-1][column+1]== currentPlayer and board[row-2][column+2]== currentPlayer and board[row-3][column+3]== currentPlayer):
                return "Winner"
    # checking for diagonal wins
    for row in range(len(board)-3):
        for column in range(4):
            if (board[row][column] == currentPlayer and board[row+1][column+1]== currentPlayer and board[row+2][column+2]== currentPlayer and board[row+3][column+3]== currentPlayer):
                return "Winner"

def conncetFour():
    board = np.zeros((6, 7))
    gameOver = False
    currentPlayer = 1
    win = ""
 
    print("-----------------------")
    print("Welcome to Connect Four")
    print("-----------------------")
    print("\n")
    print(board)

    while gameOver != True:
        if currentPlayer == 1:
            print("Player X Turn: ")
            column = int(input("Enter a number between 1 - 7: "))
            board, row = update_board(board, column, currentPlayer)
            print(row)
            print(board)
            win = checkWinner(board, currentPlayer)
            currentPlayer = 2
        elif currentPlayer == 2:
            print("Player Y Turn: ")
            column = int(input("Enter a number between 1 - 7: "))
            board, row = update_board(board, column, currentPlayer)
            print(board)
            print(row)
            win = checkWinner(board, currentPlayer)
            currentPlayer = 1

        if win == "Winner":
            print("The Winner is: ", currentPlayer)
            gameOver = True

conncetFour()


