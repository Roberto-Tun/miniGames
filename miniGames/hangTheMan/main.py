'''
Author: Roberto Tun
Date: 29/03/24
Description: Hang the man CLI game that will get the word imported and read from a file
'''
# importing random module
import random

# opening the words.txt file
words = open('miniGames/hangTheMan/words.txt','r')

# adding all the words in the file into wordslist
wordslist = words.readlines()

# creating a list to store the new words without the '\n' character
listOfWords = []

# creating an empty list to store the character of every letter in the word
emptyWordList = []

# using a for the remove the '\n' character of each word and appending it to a list
for word in wordslist:
    listOfWords.append(word.strip("\n"))

# using the random module to get a random word from the list for the user to guess
def randomWord(wordlist):
    mystoryWord = random.choice(wordlist)
    return mystoryWord

# created a function to fill the empty list with "-" for every letter in the word
def mystoryWordLength(word):
    for letter in word:
        emptyWordList.append("-")

# created a function to check if the letter is in the word and return the lives depending if the letter is or is not in the word
def checkLetter(letter, word, lives):
    if letter in word:
        for position in range(len(word)): # for used to iterate through the word 
            if word[position] == letter: # if checks that checks if the current letter matches the letter guessed
                emptyWordList[position] = letter 
        return lives
    else:
        return lives-1

# function that checks if the list no longer has "-" which means the word is complete
def checkWin():
    if "-" not in emptyWordList:
        return True

def display_hangman(lives): # function that creates the state of the hangman
    if lives == 6:
        print("|------|   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 5:
        print("|------|   ")
        print("|      O   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 4:
        print("|------|   ")
        print("|      O   ")
        print("|      |   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 3:
        print("|------|   ")
        print("|      O   ")
        print("|     /|   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 2:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 1:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|     /    ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 0:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|     / \  ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")

# main function to run the game
def hangman():
    # local variables
    gameOver = False
    mystoryWord = randomWord(listOfWords).upper() # getting the random word 
    mystoryWordLength(mystoryWord) # creating the empty list with the size of the word
    lives = 6

    print("------------------")
    print("Welcome to Hangman")
    print("------------------")
    print("\n")

    while gameOver != True:
        hidden_string = " ".join(emptyWordList) # converting the empty list to a str for better presentation
        display_hangman(lives) # displaying the man current state
        print("Current lives: ",  lives) 
        print("The Word to guess is: ", hidden_string)
        guess = input("Enter you letter guess: ").upper()
        lives = checkLetter(guess, mystoryWord, lives)
        if lives < 0:
            print("The word was: ", mystoryWord)
            gameOver = True

        if checkWin() == True:
            print("Great Job you Won!")
            gameOver = True

        
hangman()

