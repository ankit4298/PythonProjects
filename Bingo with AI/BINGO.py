import time
import os
import BingoBoard as bingo
import AI as ai
import HumanScore as human

board=[0]*26
AIboard=[0]*26


def markBox(board,no):
    block=board.index(no)
    board[block]="/"



# -----Debugging Data headers for Human and AI------
file=open("debug_data/debugdata_ai.csv","w+")
file.write("r1,r2,r3,r4,r5,c1,c2,c3,c4,c5,d1,d2,max_rwt,max_cwt,max_dwt,whr,whc_r/c/d,val_at_idx\n")
file.close()
file=open("debug_data/debugdata_human.csv","w+")
file.write("r1,r2,r3,r4,r5,c1,c2,c3,c4,c5,d1,d2,value_at_idx\n")
file.close()
# --------------------------------------------------



bingo.initializeGame(board)
bingo.initializeGame(AIboard)

# --------initialBoard Data------------------------
file=open("debug_data/initialBoard.csv","w+")
ctr=0
file.write("c1,c2,c3,c4,c5\n")
for x in range(1,26):
    file.write(str(board[x])+",")
    ctr+=1
    if(ctr%5==0):
        file.write("\n")

file.write("\n\n")
for x in range(1,26):
    file.write(str(AIboard[x])+",")
    ctr+=1
    if(ctr%5==0):
        file.write("\n")

file.close()

# ----------------------------------------


tryAgainFlag=0

game="Running"

while (game=="Running"):
    tryAgainFlag=0

    human.getScore(board)

    os.system('cls')
    bingo.updateGameBoard(board)

    # change status of isAI to False to see AI board as well
    bingo.updateGameBoard(AIboard,isAI=True)

    # HUMAN CHANCE
    try:
        z=int(input("Enter a number: "))
        # index for human board
        markBox(board,z)

        # index for aiboard for same no
        markBox(AIboard,z)

        # ----Checking human winning--------

        human.getScore(board)
        h_rw=human.row_wt
        h_cw=human.col_wt
        h_dw=human.diag_wt

        human.addToFile(z)

        if(bingo.checkWin(rw=h_rw,cw=h_cw,dw=h_dw)):
            game="Won_H"
        # ----------------------------
    except ValueError:
        tryAgainFlag=1
        print("TRY DIFFERENT NO.")
        ai.calcWeight(AIboard)


    if(tryAgainFlag==0 and game=="Running"):
        ai.calcWeight(AIboard)
        value_at_idx=ai.getAIMove(AIboard)

        # AI CHANCE
        try:
            # slash the no. which ai guessed from both boards
            markBox(board,value_at_idx)

            markBox(AIboard,value_at_idx)
            ai.calcWeight(AIboard)

            # ----Checking AI winning--------

            ai_rw=ai.row_wt
            ai_cw=ai.col_wt
            ai_dw=ai.diag_wt

            if(bingo.checkWin(rw=ai_rw,cw=ai_cw,dw=ai_dw)):
                game="Won_A"
            # ----------------------------

        except:
            print("TRY DIFFERENT NO.")

if(game=="Won_H"):
    print("Congratulations YOU WON")
elif(game=="Won_A"):
    print("You are beaten by AI")
