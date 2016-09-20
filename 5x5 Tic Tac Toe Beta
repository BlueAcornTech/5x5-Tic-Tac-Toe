import random
import time


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


def makeMove(board, letter, move):
    del board[move]
    board.insert(move, letter)
    return board


def duplicateBoard(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def inputPlayerLetter():
    letter = ''
    if letter != 'X' or letter != 'O':
        print('Do you want to be X or O ?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        if letter == 'O':
            return ['O', 'X']


def goesFirst():
    first = random.randint(1, 2)
    if first == 1:
        return 'player'
    else:
        return 'computer'


def isSpaceFree(board, move):
    if board[move] == ' ':
        return True
    else:
        return False


def isBoardFull(board):
    for i in range(1, 26):
        if isSpaceFree(board, i):
            return False
        else:
            return True


def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split():
        print('Where would you like to move')
        move = input()
    return int(move)


def isWinner(board, playerLetter):
    winner = 'nobody'
    # check row
    for i in (1, 6, 11, 16, 21):
        if board[i] == board[i + 1] and board[i] == board[i + 2] and board[i] == board[i + 3] and board[i] == board[i + 4] and board[i] != ' ':
            if board[i] == playerLetter:
                winner = 'player'
            else:
                winner = 'computer'
            return winner
    # check column
    for i in (1, 2, 3, 4, 5):
        if board[i] == board[i + 5] and board[i] == board[i + 10] and board[i] == board[i + 15] and board[i] == board[i + 20] and board[i] != ' ':
            if board[i] == playerLetter:
                winner = 'player'
            else:
                winner = 'computer'
            return winner
    # check diagonal

    if board[5] == board[9] and board[5] == board[13] and board[5] == board[17] and board[5] == board[21] and board[5] != ' ':
        if board[i] == playerLetter:
            winner = 'player'
        else:
            winner = 'computer'
        return winner


    if board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] != ' ':
        if board[i] == playerLetter:
            winner = 'player'
        else:
            winner = 'computer'
        return winner


def computerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'
    for i in range(1, 26):
        copy = duplicateBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    for i in range(1, 26):
        copy = duplicateBoard(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    if board[13] == ' ':
        return 13
    for i in (7, 9, 17, 19):
        if board[i] == ' ':
            return i
    for i in (8, 12, 18, 14):
        if board[i] == ' ':
            return i
    for i in (1, 5, 21, 25):
        if board[i] == ' ':
            return i
    for i in (6, 11, 16, 22, 23, 24, 20, 15, 10, 2, 3, 4):
        if board[i] == ' ':
            return i


playAgain = 'yes'
while playAgain == 'yes':
    print('Welcome to 5x5 Tic Tac Toe!!!')
    print('A game presented to you by Blue Acorn Tech')
    print()
    print('I am very pleased to say that this project is up and running')
    print('Please also check out other Blue Acorn Tech games!')
    time.sleep(1.5)
    print()
    print('Would you like to know how to play and use the game? (yes or no)')
    playerChoice = input()
    if playerChoice == 'yes':
        rules = displayRules()
    if playerChoice == 'no' or rules == 'read':
        theBoard = [' '] * 26
        playerLetter, computerLetter = inputPlayerLetter()
        turn = goesFirst()
        print('The ' + turn + ' will go first!')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = playerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Horray, you have beaten the computer!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        gameIsPlaying = False
                    else:
                        turn = 'computer'
            if turn == 'computer':
                move = computerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you NOOB!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        gameIsPlaying = False
                    else:
                        turn = 'player'

    print('Would you like to play again? (yes or no)')
    playAgain = input()



















