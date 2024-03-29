'''
Author: Roberto Tun
Date: 28/03/24
Description: CLI tictactoe
'''

# loop to continue playing
table = ["-","-","-",
         "-","-","-",
         "-","-","-" ]
currentPlayer = "X"

gameOver = False

# function to show user the table
def showTable():
    print(table[0] + " | " + table[1] + " | " + table[2])
    print("---------")
    print(table[3] + " | " + table[4] + " | " + table[5])
    print("---------")
    print(table[6] + " | " + table[7] + " | " + table[8])


# function to check if space is available 
def checkSpace(position, currentPlayer):
    if table[position-1] == "-":
        table[position-1] = currentPlayer
    else:
        print("Space is already taken")

 #functions that checks the different ways the user can win
def CheckWinner():
    #checks for horizontal wins
    if table[0] == table[1] == table[2] and table[0] != "-":
        Winner = table[0]
        return Winner
    elif table[3] == table[4] == table[5] and table[3] != "-":
        Winner = table[3]
        return Winner
    elif table[6] == table[7] == table[8] and table[6] != "-":
        Winner = table[6]
        return Winner
    #checks for Vertical wins
    elif table[0] == table[3] == table[6] and table[0] != "-":
        Winner = table[0]
        return Winner
    elif table[1] == table[4] == table[7] and table[1] != "-":
        Winner = table[1]
        return Winner
    elif table[2] == table[5] == table[8] and table[2] != "-":
        Winner = table[2]
        return Winner
    #checks for the X winning style
    elif table[0] == table[4] == table[8] and table[0] != "-":
        Winner = table[0]
        return Winner
    elif table[2] == table[4] == table[6] and table[2] != "-":
        Winner = table[2]
        return Winner
    #checks if it a tie
    elif "-" not in table:
        Winner = "Tie"
        return Winner

#main to play game
def tikTacToe(gameOver, currentPlayer):
    print("----------------------")
    print("Welcome to Tic-Tac-Toe")
    print("----------------------")
    print("\n")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\n")

    while gameOver != True:
        if currentPlayer == "X":
            position = int(input("Enter the position for the player X: "))
            if position > 0 and position < 10:
                checkSpace(position, currentPlayer)
            else:
                print("Position is out of bounds")
            currentPlayer = "O"
        else: 
            position = int(input("Enter the position for the player O: "))
            if position > 0 and position < 10:
                checkSpace(position, currentPlayer)
            else:
                print("Position is out of bounds")
            currentPlayer = "X"

        print("\n")
        showTable()
        print("\n")

        winner = CheckWinner()
        if winner == "X":
            print("The winner is Player X!")
            gameOver = True
        elif winner == "O":
            print("The winner is Player O")
            gameOver = True
        elif winner == "Tie":
            print(winner)
            gameOver = True


tikTacToe(gameOver, currentPlayer)
