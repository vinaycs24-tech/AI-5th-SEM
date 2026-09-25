board = [' ' for _ in range(9)]
def display_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
def player_input(player, board):
    while True:
        try:
            move = int(input(f'Player {player}, enter your move (1-9): '))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                return move - 1
            else:
                print('Invalid move. That spot is already taken or out of range. Try again.')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')

def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def check_draw(board):
    return ' ' not in board

def play_game():
    current_board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(current_board)
        move = player_input(current_player, current_board)
        current_board[move] = current_player

        if check_win(current_board, current_player):
            display_board(current_board)
            print(f'Player {current_player} wins!')
            game_over = True
        elif check_draw(current_board):
            display_board(current_board)
            print('It\'s a draw!')
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

play_game()
