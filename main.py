def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Other diagonal
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Try again.")
            continue
        if board[row][col] != " ":
            print("Position already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()