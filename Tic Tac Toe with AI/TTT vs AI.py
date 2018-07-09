'''
Tic Tac Toe game with AI
play versus COMPUTER

-----------------------------------------------
AI Reference from
https://inventwithpython.com/chapter10.html
-----------------------------------------------
'''

import time
import os
import random

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

player=1
game='Running'
mark='X'

# Winn flags
Win=1
Lose=-1
Tie=0

def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")


# winning condition
def checkWin():
    global game
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = 'Win'
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = 'Win'
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = 'Win'
    #Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = 'Win'
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = 'Win'
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game='Win'
    #Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = 'Win'
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game='Win'
    #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game='Draw'
    else:
        game='Running'


def checkPos(x):
	if(board[x]==' '):
		return True
	else:
		return False

## AI Logic ---------------------------------------------------------------------------

def isWinner(b,mark): #b is board
    return ((b[1]==mark and b[2]==mark and b[3]==mark) or
            (b[4]==mark and b[5]==mark and b[6]==mark) or
            (b[7]==mark and b[8]==mark and b[9]==mark) or
            (b[8]==mark and b[5]==mark and b[2]==mark) or
            (b[7]==mark and b[5]==mark and b[3]==mark) or
            (b[1]==mark and b[5]==mark and b[9]==mark))

def getBoardCopy(board):
    dupeboard=[]
    for i in board:
        dupeboard.append(i)
    return dupeboard

def makeMove(board, letter, move):
    board[move] = letter

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def chooseRandomMoveFromList(board,moveList):
    possibleMoves=[]
    for i in moveList:
        if checkPos(i): # if empty
            possibleMoves.append(i)

    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None


def getAIMove(mark):
    oppMark='X'

    # 1-Move with which we can win
    for i in range(1,10):
        copyBoard=getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,mark,i)
            if isWinner(copyBoard,mark):
                return i

    # 2-Move with which we can stop opp. from winning
    for i in range(1,10):
        copyBoard=getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            makeMove(copyBoard,oppMark,i)
            if isWinner(copyBoard,oppMark):
                return i

    # 3-Placing mark on corners(if empty)
    move=chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if(move != None):
        return move

    # 4-Placing mark on the center(if empty)
    if(checkPos(5)):    # if true
        return 5

    # 5-Placing mark on sides
    return chooseRandomMoveFromList(board, [2,4,6,8])


# ------------------------------------------------------------------------------------------


print("Tic-Tac-Toe")
print("Player 1 [X] --- Player 2(AI) [O]\n")

while(game=='Running'):
    os.system('cls')
    DrawBoard()
    print(game)

    if(player %2 !=0):
        print('player 1 chance')
        mark='X'
        choice=int(input('\n\nEnter choice between 1-9 '))
    else:
        print('AI chance')
        mark='O'
        choice=getAIMove(mark)
    if(checkPos(choice)):
        board[choice]=mark
        player+=1
        checkWin()


os.system('cls')
DrawBoard()

print(game)
if(player %2 ==0):
    print('player 1 won')
elif(player%2!=0):
    print('player 2 (AI) won')
