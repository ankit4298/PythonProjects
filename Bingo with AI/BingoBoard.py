import time
import random
import AI as ai


board=[0]*26
AIboard=[0]*26
rblockUsed=[]
no_overwritted=[]
no_used=[]

def displayBoard(board):
    print("| %s  | %s  | %s  | %s  | %s  |"%(board[1],board[2],board[3],board[4],board[5]))
    print("| %s  | %s  | %s  | %s  | %s  |"%(board[6],board[7],board[8],board[9],board[10]))
    print("| %s  | %s  | %s  | %s  | %s  |"%(board[11],board[12],board[13],board[14],board[15]))
    print("| %s  | %s  | %s  | %s  | %s  |"%(board[16],board[17],board[18],board[19],board[20]))
    print("| %s  | %s  | %s  | %s  | %s  |"%(board[21],board[22],board[23],board[24],board[25]))


def isEmpty(rblock):
    rblockFlag=0

    for r_blk in rblockUsed:
        if(r_blk==rblock):
            rblockFlag=1

    if(rblockFlag==1):
        return False
    else:
        return True


def fillBoard(board):
    i=1
    while i<26:
        rblock=random.randint(1,25)

        # next itr
        if(isEmpty(rblock)):
            board[rblock]=i
            rblockUsed.append(rblock)
        else:
            pass
            no_overwritted.append(i)
        i+=1


def updateZeros(board):
    i=1
    for b in board:
        if(b!=0):
            no_used.append(b)

    while(i<26):
        if(board[i]==0):
            board[i]=no_overwritted[len(no_overwritted)-1]
            no_used.append(no_overwritted[len(no_overwritted)-1])
            no_overwritted.pop()
        i+=1

def initializeGame(board):
    fillBoard(board)
    updateZeros(board)

def updateGameBoard(board,isAI=False):
    if(isAI!=True):
        displayBoard(board)


def checkWin(rw,cw,dw):
    # for winning BINGO
    # collectively rw,cw,dw should have five 5's
    score=0

    for x in rw:
        if(x==5):
            score+=1
    for x in cw:
        if(x==5):
            score+=1
    for x in dw:
        if(x==5):
            score+=1

    if(score>5):
        return True
    else:
        return False
