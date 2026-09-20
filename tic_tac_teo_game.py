# Tic-Tac-Toe Game

board = [" "] * 9

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def play_game():
    player = "X"

    for turn in range(9):
        display_board()

        print("Player", player, "turn")

        while True:
            try:
                position = int(input("Choose a position (1-9): "))

                if position < 1 or position > 9:
                    print("Please choose a number from 1 to 9.")
                elif board[position - 1] != " ":
                    print("That position is already taken.")
                else:
                    board[position - 1] = player
                    break

            except ValueError:
                print("Please enter a number.")

        if check_winner(player):
            display_board()
            print("🎉 Player", player, "wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display_board()
    print("It's a draw!")


play_game()
