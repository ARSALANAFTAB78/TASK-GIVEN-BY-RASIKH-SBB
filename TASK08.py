import math

def initialize_board():
    return [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i:i + 3] for i in range(0, len(board), 3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]        
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_draw(board):
    return ' ' not in board

def min_max(board, depth, is_maximizing):
    if is_winner(board, 'X'):  
        return 10 - depth
    if is_winner(board, 'O'):  
        return depth - 10
    if is_draw(board): 
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = min_max(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = min_max(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = -1
    best_value = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = min_max(board, 0, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe Game!")
    print("Player (O) vs AI (X)")
    print_board(board)

    while True:
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[player_move] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI's turn...")
        ai_move = get_best_move(board)
        board[ai_move] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()