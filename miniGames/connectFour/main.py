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

def checkWinner(board, row, column, currentPlayer):
    fourWin = []
    if 0 not in board:
        return "Tie"
    else:
        column = column - 1
        #checking vertical up
        if board[row-1][column] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row+1][column])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #checking vertical down
        elif board[row-1][column] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row-i][column])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #checing horizontal right
        elif board[row][column+1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row][column+i])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #checking horizontal left
        elif board[row][column-1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row][column-1])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #checing diagonal right up
        #elif board[row+1][column+1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row+i][column+1])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #elif board[row-1][column-1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row-1][column-1])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #elif board[row+1][column-1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row+1][column-1])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []
        #elif board[row-1][column+1] == currentPlayer:
            for i in range(4):
                fourWin.append(board[row-1][column+1])
            if all(ele == fourWin[0] for ele in fourWin) == True:
                return "Winner"
            else:
                fourWin = []

def conncetFour():
    board = np.zeros((6, 7))
    gameOver = False
    currentPlayer = 1
 
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
            win = checkWinner(board, row, column, currentPlayer)
            currentPlayer = 2
        elif currentPlayer == 2:
            print("Player Y Turn: ")
            column = int(input("Enter a number between 1 - 7: "))
            board, row = update_board(board, column, currentPlayer)
            print(board)
            print(row)
            win = checkWinner(board, row, column, currentPlayer)
            currentPlayer = 1

        
        if win == "Tie": 
            print("It is a tie")
            gameOver = True
        elif win == "Winner":
            print("The winner is ", currentPlayer)
            gameOver = True

conncetFour()
