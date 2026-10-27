from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    """
    Solves the N-Queens puzzle by placing N chess queens on an N x N 
    chessboard so that no two queens threaten each other.
    
    Args:
        n (int): The dimension of the board and the number of queens.
        
    Returns:
        List[List[str]]: A list of all valid board configurations, where 
                         'Q' represents a queen and '.' represents an empty space.
    """
    def backtrack(row: int):
        # Base case: If we have successfully placed a queen in every row
        if row == n:
            # Convert the current board state (list of lists) to a list of strings
            board_layout = ["".join(row_state) for row_state in board]
            result.append(board_layout)
            return

        for col in range(n):
            # Check if the current column or either diagonal is under attack
            if col in cols or (row - col) in neg_diag or (row + col) in pos_diag:
                continue
            
            # Place the queen and mark the column and diagonals as occupied
            cols.add(col)
            neg_diag.add(row - col)
            pos_diag.add(row + col)
            board[row][col] = 'Q'
            
            # Move to the next row recursively
            backtrack(row + 1)
            
            # Backtrack: Remove the queen and unmark the sets to try the next column
            cols.remove(col)
            neg_diag.remove(row - col)
            pos_diag.remove(row + col)
            board[row][col] = '.'

    result = []
    # Initialize an empty N x N board with '.'
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Sets to keep track of columns and diagonals currently under attack.
    # For positive diagonals, (row + col) remains constant.
    # For negative diagonals, (row - col) remains constant.
    cols = set()
    pos_diag = set() 
    neg_diag = set() 
    
    # Start the backtracking process from the 0th row
    backtrack(0)
    
    return result


# Example Usage:
if __name__ == "__main__":
    board_size = 4
    solutions = solveNQueens(board_size)
    
    print(f"Total valid configurations for {board_size}x{board_size} board: {len(solutions)}\n")
    
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print("-" * 15)