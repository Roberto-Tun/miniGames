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

emptyWordList = []

# using a for the remove the '\n' character of each word and appending it to a list
for word in wordslist:
    listOfWords.append(word.strip("\n"))

# using the random module to get a random word from the list for the user to guess
def randomWord(wordlist):
    mystoryWord = random.choice(wordlist)
    return mystoryWord

def mystoryWordLength(word):
    for letter in word:
        emptyWordList.append("-")

def checkLetter(letter, word, lives):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                emptyWordList[i] = letter
        return lives
    else:
        return lives-1


def checkWin():
    if "-" not in emptyWordList:
        return True

def display_hangman(lives): #function that creates the state of the hangman
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

def hangman():
    gameOver = False
    mystoryWord = randomWord(listOfWords).upper()
    mystoryWordLength(mystoryWord)
    lives = 6

    print("------------------")
    print("Welcome to Hangman")
    print("------------------")
    print("\n")

    while gameOver != True:
        hidden_string = " ".join(emptyWordList)
        print(mystoryWord)
        display_hangman(lives)
        print("Current lives: ",  lives)
        print("The Word to guess is: ", hidden_string)
        guess = input("Enter you letter guess: ").upper()
        lives = checkLetter(guess, mystoryWord, lives)
        print(emptyWordList)
        if lives < 0:
            print("The word was: ", mystoryWord)
            gameOver = True

        if checkWin() == True:
            print("Great Job you Won!")
            gameOver = True

        
hangman()

