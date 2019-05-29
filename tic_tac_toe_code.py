from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |   ')

def player_input():
    marker = ''
    # Keep asking to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, please pick X or O: ')
    
    # Assign Player 2 the opposite marker
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    play_again = input('Do you want to play again?: ')
    return play_again.lower()[0] == 'y'


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')

#while True:
while True:
    theboard = [' '] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first!')
    
    game_on = input('Are you ready to start the game?')
    if game_on.lower()[0] == 'y':
        game_on == True
    else:
        game_on == False

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player1_marker,position)
            
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congratulations, Player 1 is the winner!')
                game_on = False
            elif not win_check(theboard,player1_marker) and full_board_check(theboard):
                display_board(theboard)
                print("It's a tie!")
                break
            else:
                turn = 'Player 2'
        
        
        # Player2's turn.
        else:  
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player2_marker,position)
            
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('Congratulations, Player 2 is the winner!')
                game_on = False
            elif not win_check(theboard,player2_marker) and full_board_check(theboard):
                display_board(theboard)
                print("It's a tie!")
                break
            else:
                turn = 'Player 1'

    if not replay():
        print("Thanks for playing!")
        break