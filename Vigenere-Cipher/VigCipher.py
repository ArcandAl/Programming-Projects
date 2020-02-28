# Alec Arcand
import os
from os.path import exists



def main():
    print('Welcome to the Vigenere-cipher Encryption/Decryption Program''\n')

    charDict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, \
    'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, \
    'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, ' ' : 26, '\n' : 27, ',' : 28, \
    '.' : 29, '?' : 30, '!' : 31 }
    valid = True
    while valid:
        validChoice = ['e', 'd', 'x']
        choice = input("Would you like to (e)ncryot a file, (d)ecrpt a file, or e(x)it (enter e, d, or x)? ")
        while choice not in validChoice:
            choice = input("Sorry, that's an invalid choice. Please enter only e, d, or x: ")
        if choice == 'e':
            encrypt(charDict)
        if choice == 'd':
            decrypt(charDict)
        if choice == 'x':
            valid = False


def encrypt(charDict):
    mode = 'enc'
    keyword = input("What keyword would you like to use for encryption? ")
    fileName = input("Enter the text-file name to encrypt: ")
    while not exists(fileName):
        print('Sorry the file', "'",fileName,"'", 'does NOT exist -- please try again!')
        fileName = input("Enter the test-file name to encrypt: ")
    calculate(keyword, charDict, fileName, fileName.replace('.txt', '.zzz'), mode)
    print('The file', "'",fileName,"'", 'was successfully encrypted using keyword', "'",keyword,"'", 'to the file', fileName.replace('.txt', '.zzz'))

def decrypt(charDict):
    mode = 'dec'
    keyword = input("What keyword would you like to use for decryption: ")
    deFile = input('Enter the text-file name to decrypt: ')
    while not exists(deFile.replace('.zzz', '.txt')):
        print('Sorry the file', "'",deFile,"'", 'does NOT exist -- please try again!')
        deFile = input("Enter the text-file name to decrypt: ")
    if exists(deFile.replace('.zzz', '.txt')):
        print('WARNING:    The file', "'",deFile.replace('.zzz', '.txt'),"'", 'already exists!')
        choose = input('Is it okay to wip it out (y/n)? ')
        if choose == 'n':
            fileName = input('Enter the file name tht should be used (.txt extension will automatically be added): ') + ('.txt')
            while not exists(fileName):
                print('Sorry the file', "'",fileName,"'", 'does NOT exist -- please try again!')
                fileName = input('Enter the file name tht should be used (.txt extension will automatically be added): ') + ('.txt')
            calculate(keyword, charDict, deFile, fileName, mode)
            print('The file', "'",deFile,"'", 'was successfully decrypted using keyword', "'",keyword,"'", 'to file', "'",fileName,"'")
        else:
            calculate(keyword, charDict, deFile, deFile, mode)
            print('The file', "'",deFile,"'", 'was successfully decrypted using keyword', "'",keyword,"'", 'to file', "'",deFile,"'")

def calculate(keyword, charDict, readFile, writeFile, mode):
    newFile = open(writeFile, 'w')
    message = open(readFile, 'r')
    stringFile = message.read().casefold()
    messageCharIndex = 0
    for character in stringFile:
        keywordCharIndex = messageCharIndex % len(keyword)
        if mode == 'enc':
            if character in charDict:
                num = (charDict[character] + charDict[keyword[keywordCharIndex]]) % len(charDict)
                for i in charDict:
                    if charDict[i] == num:
                        newFile.write(i)
                        messageCharIndex += 1
            else:
                messageCharIndex = messageCharIndex
        if mode == 'dec':
            if character in charDict:
                num = (charDict[character] - charDict[keyword[keywordCharIndex]]) % len(charDict)
                for i in charDict:
                    if charDict[i] == num:
                        newFile.write(i)
                        messageCharIndex += 1
            else:
                messageCharIndex = messageCharIndex




main()
