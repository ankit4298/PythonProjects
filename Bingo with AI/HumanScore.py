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

def getScore(board):
    checkRow(board)
    checkColumn(board)
    checkDiagonal(board)

    for x in range(1,26):
        if(board[x]=="/"):
            board[x]="*"

def addToFile(no):
    # ------Debug Human Data------------------
    file=open("debug_data/debugdata_human.csv","a+")

    file.write("\n"+str(row_wt[1:]))
    file.write(","+str(col_wt[1:]))
    file.write(","+str(diag_wt[1:]))

    file.write(","+str(no)) # value_at_idx

    file.close()
    # -----------------------------------------
