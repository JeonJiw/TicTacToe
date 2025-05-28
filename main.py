from game import initialize_board, print_board, user_move, check_win, is_full
from ai import computer_move

def play_game():
    stats = {"wins": 0, "losses": 0, "ties": 0}
    while True:
        board = initialize_board()
        print("Tic-Tac-Toe: You (X) vs Computer (O)")
        
        while True:
            print_board(board)
            user_move(board)
            if check_win(board, "X"):
                print_board(board)
                print("You win!")
                stats["wins"] += 1
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                stats["ties"] += 1
                break

            computer_move(board)
            if check_win(board, "O"):
                print_board(board)
                print("Computer wins!")
                stats["losses"] += 1
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                stats["ties"] += 1
                break

        print(f"\nStats → Wins: {stats['wins']}, Losses: {stats['losses']}, Ties: {stats['ties']}")
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    play_game()