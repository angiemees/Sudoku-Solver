import random
import solver

def generateBoard(difficulty="medium") -> list:

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    solver.SudokuSolver(board)

    if difficulty == "easy":
        cells_to_remove = 20
    elif difficulty == "medium":
        cells_to_remove = 30
    elif difficulty == "hard":
        cells_to_remove = 40
    else:
        cells_to_remove = 30 
    
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    
    def count_solutions(board):
        count = [0]
        
        def solver_count(board):
            empty_cell = solver.findEmptyCell(board)
            if not empty_cell:
                count[0] += 1
                return count[0] > 1
            row, col = empty_cell
            
            for number in range(1, 10):
                if solver.isValid(board, number, col, row):
                    board[row][col] = number
                    if solver_count(board):
                        return True
                    board[row][col] = 0
            return False
        
        solver_count(board)
        return count[0]
    
    
    num_removed = 0
    for r, c in positions:
        
        original_value = board[r][c]
        board[r][c] = 0
        
        
        if count_solutions(board) > 1:
            
            board[r][c] = original_value
        else:
            num_removed += 1
        
        
        if num_removed >= cells_to_remove:
            break
    
    return board

#if __name__ == "__main__":
#    board = generateBoard(difficulty="medium")
#    for row in board:
#        print(row)
