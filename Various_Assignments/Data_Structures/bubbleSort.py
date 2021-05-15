'''
    Description:  Sorts myList in ascending order using a bubble sort.
    File:  bubbleSort.py
'''

def bubbleSort(myList):
    """Rearranges the items in myList so they are in ascending order"""
    for lastUnsortedIndex in range(len(myList)-1,0,-1):
        # scan the Before sorting part at the beginning of myList
        for testIndex in range(lastUnsortedIndex):
            # if we find two adjacent items out of order, switch them
            if myList[testIndex] > myList[testIndex+1]:
                temp = myList[testIndex]
                myList[testIndex] = myList[testIndex+1]
                myList[testIndex+1] = temp
                print(myList)

aList = [4,3,2,10,12,1,5,6]
bubbleSort(aList)
