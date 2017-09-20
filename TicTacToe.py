from __future__ import print_function

from IPython.display import clear_output

def DisplayBoard(board):

    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
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
