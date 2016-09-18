import random

def displayRules():
    print('You definetley know how to play actual Tic Tac Toe')
    print('In 5x5 Tic Tac Toe you must get a 5 in a row')
    print('To describe where you want to place an X or an O')
    print('Refer to the following board')
    print('    |    |    |    |    ')
    print(' ' + '21' + ' | ' + '22' + ' | ' + '23' + ' | ' + '24 ' + '| ' + '25')
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + '16' + ' | ' + '17' + ' | ' + '18' + ' | ' + '19' + ' | ' + '20')
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + '11' + ' | ' + '12' + ' | ' + '13' + ' | ' + '14' + ' | ' + '15')
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + '6' + '  | ' + '7' + '  | ' + '8' + '  | ' + '9' + '  | ' + '10')
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + '1' + '  | ' + '2' + '  | ' + '3' + '  | ' + '4' + '  | ' + '5')
    print('    |    |    |    |')
    print('So if you want to place an X or an O within a certain box, just input that box\'s number reference')
    print('Good luck!')
    return 'read'


def drawBoard(board):
    print('    |    |    |    |    ')
    print(' ' + board[21] + '  | ' + board[22] + '  | ' + board[23] + '  | ' + board[24] + '  | ' + board[25])
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + board[16] + '  | ' + board[17] + '  | ' + board[18] + '  | ' + board[19] + '  | ' + board[20])
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + board[11] + '  | ' + board[12] + '  | ' + board[13] + '  | ' + board[14] + '  | ' + board[15])
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + board[6] + '  | ' + board[7] + '  | ' + board[8] + '  | ' + board[9] + '  | ' + board[10])
    print('    |    |    |    |')
    print('------------------------')
    print('    |    |    |    |    ')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3] + '  | ' + board[4] + '  | ' + board[5])
    print('    |    |    |    |')


def inputPlayerLetter():
    letter = ''
    if letter != 'X' or letter!= 'O':
        print('Do you want to be X or O ?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        if letter == 'O':
            return ['O', 'X']

def goesFirst():
    first = random.randint(1,2)
    if first == 1:
        return 'player'
    else:
        return 'computer'

def isWinner(bo, le):
    return ((bo[21] == le and bo[22] == le and bo[23] == le and bo[24] == le and bo[25] == le) or (bo[16] == le and bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or (bo[11] == le and bo[12] == le and bo[13] == le and bo[14] == le and bo[15] == le) or (bo[6] == le and bo[7] == le and bo[8] == le and bo[9] == le and bo[10] == le) or (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or (bo[21] == le and bo[16] == le and bo[11] == le and bo[6] == le and bo[1] == le) or (bo[22] == le and bo[17] == le and bo[12] == le and bo[7] == le and bo[2] == le) or bo[23] == le and bo[18] == le and bo[13] == le and bo[8] == le and bo[3] == le) or (bo[24] == le and bo[19] == le and bo[14] == le and bo[9] == le and bo[4] == le) or (bo[25] == le and bo[20] == le and bo[15] == le and bo[10] == le and bo[5] == le) or (bo[5] == le and bo[9] == le and bo[13] == le and bo[17] == le and bo[21] == le) or (bo[1] == le and bo[7] == le and bo[13] == le and bo[19] == le and bo[25] == le)

def makeMove(board, letter, move):
    board[move] = letter

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
        return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split() or not isSpaceFree(board, int(move)):
        print('What is your move (1-25)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 26):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    if move != None:
        return move
    if isSpaceFree(board, 13):
        return 13

def isBoardFull(board):
    for i in range(1, 26):
        if isSpaceFree(board, i):
            return False
        else:
            return True


print('Welcome to 5x5 Tic Tac Toe!')
print('A game presented to you by Blue Acorn Tech')
playAgain = 'yes'
while playAgain == 'yes':
    print('Would you like to read the rules of 5x5 Tic Tac Toe?')
    playerChoice = input()
    if playerChoice == 'yes':
        rules = displayRules()
    if playerChoice == 'no' or rules == 'read':
        theBoard = [' '] * 26
        playerLetter, computerLetter = inputPlayerLetter()
        turn = goesFirst()
        print('The ' + turn + ' will go first')
        gameIsPlaying = True
        while gameIsPlaying == True:
            if turn == 'player':
                drawBoard(theBoard)
                move = getPlayerMove()
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Horray, you have beaten the computer!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you NOOB!!!!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                    else:
                        turn = 'player'

    print('Would you like to play again? (Yes or No)')
    playAgain = input()

exit()
