import random
# create game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer = "X"

winner = None
gameRunning = True
# print board
def printBoard(board):
    print(board[0] + " | "+board[1] + " | "+board[2] )
    print("----------")
    print(board[3] + " | "+board[4] + " | "+board[5] )
    print("----------")
    print(board[6] + " | "+board[7] + " | "+board[8] )
# take player input 1 to 9
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot!")
# check winning status
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[1] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[3] != "-":
        winner = board[2]
        return True
# check tie status
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The Winner is {winner}")
        printBoard(board)
        gameRunning = False
# a dummy bot for opponent
def computer(board):
    while currentPlayer == "O":
        positon = random.randint(0,8)
        if board[positon] == "-":
            board[positon] = "O"
            switchPlayer()
# switch player X to O or O to X
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
# runs the game
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)


