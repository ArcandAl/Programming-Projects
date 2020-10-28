"""
Author: Alec Arcand
Minimax algorithm implemented to solve 
the game Mancala. The Mancala board is represented
by a string.
"""

def makeMove(board, position):
    boardCopy = board.copy()
    if position == -1:
        return boardCopy
    marbles = boardCopy[position]
    if marbles == 0:
        return board
    bLength = len(boardCopy) - 1
    boardCopy[position] = 0
    while marbles != 0:
        if position == bLength:
            return boardCopy
        boardCopy[position + 1] = boardCopy[position + 1] + 1
        marbles = marbles - 1
        position = position + 1

    return boardCopy

def possibleMoves(board):
    possible = []
    index = 0
    for i in board:
        if i != 0:
            possible.append(index)
        index = index + 1
    return possible

def isEmpty(board):
    for i in board:
        if i != 0:
            return False
    return True

def MiniMax(board, move, isMax):
    newBoard = makeMove(board, move)

    if isEmpty(newBoard):
        if isMax:
            return (move, -1) # Min win
        else:
            return (move, 1)  # Max win

    if isMax:
        highest = float('-inf')

        for pos in possibleMoves(newBoard):
            tmp = MiniMax(newBoard, pos, not isMax)
            if tmp[1] > highest:
                highest = tmp[1]
                move = pos
        return (move, highest)
    else:
        lowest = float('inf')

        for pos in possibleMoves(newBoard):
            tmp = MiniMax(newBoard, pos, not isMax)
            if tmp[1] < lowest:
                lowest = tmp[1]
                move = pos
        return (move, lowest)

def search(board):
    lstBoard = [int(i) for i in board]

    score = MiniMax(lstBoard, -1, True)

    if score[1] == 1:
        result = "win"
    else:
        result = "lose"

    solution = (score[0] + 1, result)

    return solution
