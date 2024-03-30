'''
Author: Roberto Tun
Date: 29/03/24
Description: Hang the man CLI game that will get the word imported and read from a file
'''
# opening the words.txt file
words = open('words.txt','r')

# adding all the words in the file into wordslist
wordslist = words.readlines()

for word in wordslist:
    print(word)
