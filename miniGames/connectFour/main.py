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

def show_board(board):
    print("\n")
    print(" |1||2||3||4||5||6||7|")
    print(board)

def update_board(board, placement, currentPlayer):
    column = board[:,(placement-1)] #acces to the column trying to update
    for row in reversed(range(len(column))): #iterating through the column
        if column[row] == 0: 
            column[row] = currentPlayer
            break
    board[:, placement-1] = column
    return board

def checkWinner(board, currentPlayer):
    # checking for horizontal wins
    for row in range(6):
        for column in range(4):
            if board[row][column] == currentPlayer and board[row][column+1] == currentPlayer and board[row][column+2] == currentPlayer and board[row][column+3] == currentPlayer:
                return currentPlayer
    # checking for vertical wins
    for column in range(7):
        for row in range(3):
            if board[row][column] == currentPlayer and board[row+1][column] == currentPlayer and board[row+2][column] == currentPlayer and board[row+3][column] == currentPlayer:
                return currentPlayer
    #checking diagonal wins
    for row in range(3):
        for column in range(3, 7):
            if board[row][column] == currentPlayer and board[row+1][column-1] == currentPlayer and board[row+2][column-2] == currentPlayer and board[row+3][column-3] == currentPlayer:
                return currentPlayer
    #checking diagonal wins
    for row in range(3):
        for column in range(4):
            if board[row][column] == currentPlayer and board[row+1][column+1] == currentPlayer and board[row+2][column+2] == currentPlayer and board[row+3][column+3] == currentPlayer:
                return currentPlayer


def conncetFour():
    board = np.zeros((6, 7))
    gameOver = False
    currentPlayer = 1
    playerOneTurns = 21
    playerTwoTurns = 21
 
    print("-----------------------")
    print("Welcome to Connect Four")
    print("-----------------------")
    show_board(board)

    while gameOver != True:
        if currentPlayer == 1 and playerOneTurns > 0:
            print("Player X Turn: ")
            column = int(input("Enter a number between 1 - 7: "))
            columnCheck = board[:,(column-1)]
            if 0 not in columnCheck:
                print("Position is full")
            elif column >= 1 and column <= 7:
                board = update_board(board, column, currentPlayer)
            show_board(board)
            win = checkWinner(board, currentPlayer)
            currentPlayer = 2
            playerOneTurns -= 1
        elif currentPlayer == 2 and playerTwoTurns > 0:
            print("Player Y Turn: ")
            column = int(input("Enter a number between 1 - 7: "))
            columnCheck = board[:,(column-1)]
            if 0 not in columnCheck:
                print("Position is full")
            elif column >= 1 and column <= 7:
                board = update_board(board, column, currentPlayer)
            show_board(board)
            win = checkWinner(board, currentPlayer)
            currentPlayer = 1
            playerTwoTurns -= 1
        else:
            print("Its a tie")
            gameOver = True

        if win == 1:
            print("The Winner is: Player One")
            gameOver = True
        elif win == 2:
            print("The Winner is Player Two")
            gameOver = True
        


conncetFour()
