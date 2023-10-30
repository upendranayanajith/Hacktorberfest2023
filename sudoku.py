import random

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Check if the number is already in the row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku(board, difficulty):
    # Generate a solved Sudoku board
    solve_sudoku(board)

    # Remove numbers to create the puzzle based on difficulty level
    to_remove = 45 if difficulty == "easy" else 55 if difficulty == "medium" else 60 if difficulty == "hard" else 65
    for _ in range(to_remove):
        while True:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                break

if __name__ == "__main__":
    board = [[0] * 9 for _ in range(9)]

    # Generate a Sudoku puzzle
    generate_sudoku(board, "medium")

    print("Sudoku Puzzle:")
    print_board(board)

    # Solve the puzzle
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists for this Sudoku puzzle.")
