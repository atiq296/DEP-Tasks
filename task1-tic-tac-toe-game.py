def print_board(board):
    for row in board:
        print(" ".join(row))

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
     for row in board:
        if row.count("X") == 3:
            return -10
        elif row.count("O") == 3:
            return 10

     for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return -10
            elif board[0][col] == "O":
                return 10

     if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == "X":
            return -10
        elif board[1][1] == "O":
            return 10

     return 0  # No winner (draw)

def minimax(board, depth, isMaximizingPlayer):
     if depth == 0 or not is_moves_left(board):
        return evaluate(board)

     if isMaximizingPlayer:
        bestVal = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    value = minimax(board, depth - 1, False)
                    bestVal = max(bestVal, value)
                    board[i][j] = " "
        return bestVal
     else:
        bestVal = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    value = minimax(board, depth - 1, True)
                    bestVal = min(bestVal, value)
                    board[i][j] = " "
        return bestVal


def find_best_move(board):
    best_move = None
    best_score = float("-inf")

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while is_moves_left(board):
        print_board(board)
        user_row, user_col = map(int, input("Enter your move (row col): ").split())
        board[user_row][user_col] = "X"

        if not is_moves_left(board):
            break

        comp_row, comp_col = find_best_move(board)
        board[comp_row][comp_col] = "O"

    print_board(board)
    print("Game Over!")

if __name__ == "__main__":
    main()