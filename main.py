from game import initialize_board, print_board, user_move, computer_move, check_win, is_full

def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe: You (X) vs Computer (O)")

    while True:
        print_board(board)
        user_move(board)
        if check_win(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        computer_move(board)
        if check_win(board, "O"):
            print_board(board)
            print("Computer wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()