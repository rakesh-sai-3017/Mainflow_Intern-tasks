import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        if line.count('X') == 3:
            return 'X'
        if line.count('O') == 3:
            return 'O'
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Human starts
    
    while True:
        print_board(board)
        if current_player == 'X':
            print("Your turn (X)")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != ' ':
                print("Cell already occupied!")
                continue
            board[row][col] = 'X'
        else:
            print("AI's turn (O)")
            row, col = find_best_move(board)
            board[row][col] = 'O'
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
