def initialize_board():
    return [str(i) for i in range(1, 10)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def is_full(board):
    return all(cell in ["X", "O"] for cell in board)

def user_move(board):
    while True:
        try:
            move = int(input("Choose a position (1–9): ")) - 1
            if board[move] not in ["X", "O"]:
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")