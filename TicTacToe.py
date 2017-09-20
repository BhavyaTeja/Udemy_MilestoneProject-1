#Importing the Libraries

from __future__ import print_function

from IPython.display import clear_output

import random

def DisplayBoard(board):

    clear_output()
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def PlayerInput():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Enter your choice "X" or "O": ')
        marker = marker.upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def MarkerPosition(board, marker, position):

    board[position] = marker

def ChooseFirst():

    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def WinCheck(board, mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def SpaceCheck(board, position):

    return board[position] == ' '

def FullBoardCheck(board):

    for i in range(1,10):
        if SpaceCheck(board, i):
            return False
    return True


def PlayerChoice(board):

    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not SpaceCheck(board, int(position)):
        position = input("That's a Wrong input! Choose your next position again: (1-9) ")
    return int(position)


def Replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    Board = [' '] * 10
    player1_marker, player2_marker = PlayerInput()
    turn = ChooseFirst()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            DisplayBoard(Board)
            position = PlayerChoice(Board)
            MarkerPosition(Board, player1_marker, position)

            if WinCheck(Board, player1_marker):
                DisplayBoard(Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if FullBoardCheck(Board):
                    DisplayBoard(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            DisplayBoard(Board)
            position = PlayerChoice(Board)
            MarkerPosition(Board, player2_marker, position)

            if WinCheck(Board, player2_marker):
                DisplayBoard(Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if FullBoardCheck(Board):
                    DisplayBoard(Board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not Replay():
        break