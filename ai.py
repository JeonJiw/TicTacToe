from game import check_win, is_full

def evaluate(board):
    if check_win(board, "O"):
        return 1
    elif check_win(board, "X"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "O") or check_win(board, "X") or is_full(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] not in ["X", "O"]:
                original = board[i]
                board[i] = "O"
                eval_score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = original
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] not in ["X", "O"]:
                original = board[i]
                board[i] = "X"
                eval_score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = original
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

def computer_move(board):
    best_score = -float('inf')
    best_move = None

    for i in range(9):
        if board[i] not in ["X", "O"]:
            original = board[i]
            board[i] = "O"
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = original
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"