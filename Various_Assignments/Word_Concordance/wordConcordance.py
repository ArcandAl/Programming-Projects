from chaining_dictionary import ChainingDict
from open_addr_hash_dictionary import OpenAddrHashDict
from avl_tree import AVLTree
from binary_search_tree import BinarySearchTree
from time import clock

def main():
    stopWordDict = ChainingDict(2**15)
    #stopWordDict = OpenAddrHashDict(2**15, hash, True) #linear
    #stopWordDict = OpenAddrHashDict(2**15, hash, False) #Quadratic
    #stopWordDict = AVLTree()
    #stopWordDict = BinarySearchTree()
    stopWords = open('stop_words.txt', 'r')
    for line in stopWords:
        line = line.lower().strip('\n')
        stopWordDict[line] = []

    wordConcordanceDict = ChainingDict(2**15)
    #wordConcordanceDict = OpenAddrHashDict(2**15, hash, True) #linear
    #wordConcordanceDict = OpenAddrHashDict(2**15, hash, False) #Quadratic
    #wordConcordanceDict = AVLTree()
    #wordConcordanceDict = BinarySearchTree()
    text = open('WarAndPeace.txt', 'r')


    lineCounter = 1
    for line in text:
        line = line.rstrip()
        line = line.casefold()
        processLine(lineCounter, line, wordConcordanceDict, stopWordDict)
        lineCounter += 1
        #print(lineCounter)

    formatted(wordConcordanceDict)

def processLine(lineCounter, line, wordConcordanceDict, stopWordDict):
    wordList = createWordList(line)
    for word in wordList:
        word = word.strip("`1234567890-=~!@#$%^&*()_+;:,./<>?'\"\\|")
        if word != "" and word not in stopWordDict:
            if word in wordConcordanceDict:
                wordConcordanceDict[word].append(lineCounter)
            else:
                wordConcordanceDict[word] = [lineCounter]

def createWordList(line):
    wordList = []
    for i in line.split():
        wordList.append(i)
    return(wordList)

def formatted(wordConcordanceDict):
    outputFile = open('wordConcordance.txt', 'w')
    outputFile.write('%-20s %-15s \n' % ('Word', "Line Number(s)"))
    outputFile.write('-'*30+'\n')
    for key in sorted(wordConcordanceDict):
        outputFile.write('%-20s %-15s \n' % (key, wordConcordanceDict[key]))

if __name__ == '__main__':
    start = clock()
    main()
    end = clock()
    runtime = end - start
    print(runtime)
