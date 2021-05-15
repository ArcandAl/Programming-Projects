from cursor_based_list import CursorBasedList
from os.path import exists
import os

def main():
    print("Welcome to a simple text editor program that loads a text file into a cursor based list!")
    print()
    print("What is your choice?")
    print("O - open an existing file to edit")
    print("N - create a new text file to edit")
    print()
    choice = input("Enter your choice: ").upper()
    while choice != 'O' and choice != 'N':
        print("Invalid choice! Please select one of the choices!")
        choice = input("Enter your choice: ").upper()
    if choice == 'O':
        filename = input("Enter a text-file name to edit: ")
        while not exists(filename):
            print("File", filename, "does NOT exist!")
            filename = input("Please enter a valid filename: ")
        newFile = open(filename, 'r')
        lines = newFile.readlines()
        fileInList = CursorBasedList()
        for i in lines:
            fileInList.insertAfter(i)
    elif choice == 'N':
        filename = input("Enter what you want your text file to be named: ")
        fileInList = CursorBasedList()
        newFile = open(filename, 'w')

    while True:
        print("\n===============================================================")
        print("Text-editor menu choices: ")
        print()
        print("F - navigate and display the first line")
        print("L - navigate and display the last line")
        print("C - navigate and display the current line")
        print("N - navigate and display the next line")
        print("P - navigate and display the previous line")
        print("B - insert new line before the current line")
        print("A - insert new line after the current line")
        print("D - delete the current line")
        print("R - replace the current line with a new line")
        print("S -  save the current list back to the text file")
        print("X - quit and exit the text editor program")

        response = input("Please choose an option: ").upper()
        if response == 'F':
            firstline = fileInList.first()
            print("The first line is: ", fileInList.getCurrent())
        elif response == 'L':
            lastline = fileInList.last()
            print("The last line is: ", fileInList.getCurrent())
        elif response == 'C':
            line = fileInList.getCurrent()
            print('The current line is: ', line)
        elif response == 'N':
            if fileInList.hasNext:
                nextLine = fileInList.next()
                print("The next line is: ", fileInList.getCurrent())
            else:
                print("There is no next line in the file!")
        elif response == 'P':
            line = fileInList.previous()
            print("The previous line is: ", fileInList.getCurrent())
        elif response == 'B':
            line = input("Enter the new line to insert before the current line: ")
            line = line + '\n'
            fileInList.insertBefore(line)
        elif response == 'A':
            line = input("Enter new line to insert after the current line: ")
            line = line + '\n'
            fileInList.insertAfter(line)
        elif response == 'D':
            fileInList.remove()
        elif response == 'R':
            line = input("Enter the line you want to add: ")
            line = line + '\n'
            fileInList.replace(line)
        elif response == 'S':
            saveFile = open(filename, 'w')
            fileInList.first()
            current = fileInList.getCurrent()
            for i in range(len(fileInList)):
                saveFile.write(str(current))
                current = fileInList.next()
                current = fileInList.getCurrent()
                print(current)
        elif response == 'X':
            break
        else:
            print("Invalid menu choice!")



main()
