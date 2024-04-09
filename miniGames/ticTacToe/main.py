'''
Author: Roberto Tun
Date: 28/03/24
Description: CLI tictactoe
'''


class TicTacToe:
    def __init__(self, table, currentPlayer, gameOver):
        self.table = table
        self.currentPlayer = currentPlayer
        self.gameOver = gameOver



    # loop to continue playing
    self.table = ["-","-","-",
            "-","-","-",
            "-","-","-" ]
    currentPlayer = "X"

    gameOver = False

    # function to show user the self.table
    def showtable(self):
        print(self.table[0] + " | " + self.table[1] + " | " + self.table[2])
        print("---------")
        print(self.table[3] + " | " + self.table[4] + " | " + self.table[5])
        print("---------")
        print(self.table[6] + " | " + self.table[7] + " | " + self.table[8])


    # function to check if space is available 
    def checkSpace(self, position, currentPlayer):
        if self.table[position-1] == "-":
            self.table[position-1] = currentPlayer
        else:
            print("Space is already taken")

    #functions that checks the different ways the user can win
    def CheckWinner(self):
        #checks for horizontal wins
        if self.table[0] == self.table[1] == self.table[2] and self.table[0] != "-":
            Winner = self.table[0]
            return Winner
        elif self.table[3] == self.table[4] == self.table[5] and self.table[3] != "-":
            Winner = self.table[3]
            return Winner
        elif self.table[6] == self.table[7] == self.table[8] and self.table[6] != "-":
            Winner = self.table[6]
            return Winner
        #checks for Vertical wins
        elif self.table[0] == self.table[3] == self.table[6] and self.table[0] != "-":
            Winner = self.table[0]
            return Winner
        elif self.table[1] == self.table[4] == self.table[7] and self.table[1] != "-":
            Winner = self.table[1]
            return Winner
        elif self.table[2] == self.table[5] == self.table[8] and self.table[2] != "-":
            Winner = self.table[2]
            return Winner
        #checks for the X winning style
        elif self.table[0] == self.table[4] == self.table[8] and self.table[0] != "-":
            Winner = self.table[0]
            return Winner
        elif self.table[2] == self.table[4] == self.table[6] and self.table[2] != "-":
            Winner = self.table[2]
            return Winner
        #checks if it a tie
        elif "-" not in self.table:
            Winner = "Tie"
            return Winner

    #main to play game
    def tikTacToe(self, gameOver, currentPlayer):
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
            showtable()
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

