import random

row_wt=[0]*6
col_wt=[0]*6
diag_wt=[0]*3

def checkRow(board):
    for i in range(1,6):
        if(board[i]=="/"):
            row_wt[1]+=1

    for i in range(6,11):
        if(board[i]=="/"):
            row_wt[2]+=1

    for i in range(11,16):
        if(board[i]=="/"):
            row_wt[3]+=1

    for i in range(16,21):
        if(board[i]=="/"):
            row_wt[4]+=1

    for i in range(21,26):
        if(board[i]=="/"):
            row_wt[5]+=1

def checkColumn(board):
    z=1
    for i in range(1,6):
        if(board[z]=="/"):
            col_wt[1]+=1
        z+=5

    z=2
    for i in range(1,6):
        if(board[z]=="/"):
            col_wt[2]+=1
        z+=5

    z=3
    for i in range(1,6):
        if(board[z]=="/"):
            col_wt[3]+=1
        z+=5

    z=4
    for i in range(1,6):
        if(board[z]=="/"):
            col_wt[4]+=1
        z+=5

    z=5
    for i in range(1,6):
        if(board[z]=="/"):
            col_wt[5]+=1
        z+=5

def checkDiagonal(board):
    z=1
    for i in range(1,6):
        if(board[z]=="/"):
            diag_wt[1]+=1
        z+=6

    z=5
    for i in range(1,6):
        if(board[z]=="/"):
            diag_wt[2]+=1
        z+=4

def calcWeight(board):
    checkRow(board)
    checkColumn(board)
    checkDiagonal(board)

    for x in range(1,26):
        if(board[x]=="/"):
            board[x]="*"


def compareTO(a,b,c):
    idx=0
    z=max(a,b,c)

    # marking priority
    # 1-Diagonal, 2-Row, 3-Column

    if(z==b):   # COL
        idx=col_wt.index(b)
        x="col"

    if(z==a):   # ROW
        idx=row_wt.index(a)
        x="row"

    if(z==c):   # DIAG
        idx=diag_wt.index(c)
        x="diag"

    return x,idx

def doMove(which_move,idx,board):
    value_at_idx=0

    if(which_move=="row"):

        if(idx==2):
            idx=6
        elif(idx==3):
            idx=11
        elif(idx==4):
            idx=16
        elif(idx==5):
            idx=21

        z=idx
        stop_flag=1
        for i in range(1,6):
            if(board[z]!="/" and board[z]!="*"):
                if(stop_flag!=0):
                    value_at_idx=board[z]
                    stop_flag=0
            z+=1

    if(which_move=="col"):
        z=idx
        stop_flag=1
        for i in range(1,6):
            if(board[z]!="/" and board[z]!="*"):
                if(stop_flag!=0):
                    value_at_idx=board[z]
                    stop_flag=0
            z+=5

    if(which_move=="diag"):
        if(idx==2):
            idx=5

        z=idx
        stop_flag=1
        for i in range(1,6):
            if(board[z]!="/" and board[z]!="*"):
                if(stop_flag!=0):
                    value_at_idx=board[z]
                    stop_flag=0
            if(idx==1):
                z+=6
            else:
                z+=4

    return value_at_idx

def getMax(wts):
    max=wts[0]
    for x in wts:
        if(max<x and x!=5):
            max=x

    return max

def getAIMove(board):

    max_row_wt=getMax(row_wt)
    max_col_wt=getMax(col_wt)
    max_diag_wt=getMax(diag_wt)

    whc_move=compareTO(max_row_wt,max_col_wt,max_diag_wt)

    value_at_idx=doMove(whc_move[0],whc_move[1],board)

    # # -----------------------------
    # # Debug AI Data

    file=open("debug_data/debugdata_ai.csv","a+")

    file.write("\n"+str(row_wt[1:]))
    file.write(","+str(col_wt[1:]))
    file.write(","+str(diag_wt[1:]))

    file.write(","+str(max_row_wt))
    file.write(","+str(max_col_wt))
    file.write(","+str(max_diag_wt))

    file.write(","+str(whc_move[0]))
    file.write(","+str(whc_move[1]))
    file.write(","+str(value_at_idx))

    file.close()

    # -----------------------------

    return value_at_idx
