sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 8]]

sudoku_ok = [[8, 3, 5, 4, 1, 6, 9, 2, 7], [2, 9, 6, 8, 5, 7, 4, 3, 1],
             [4, 1, 7, 2, 9, 3, 6, 5, 8], [5, 6, 9, 1, 3, 4, 7, 8, 2],
             [1, 2, 3, 6, 7, 8, 5, 4, 9], [7, 4, 8, 5, 2, 9, 1, 6, 3],
             [6, 5, 2, 7, 8, 1, 3, 9, 4], [9, 8, 1, 3, 4, 5, 2, 7, 6],
             [3, 7, 4, 9, 6, 2, 8, 1, 5]]


#validate row
def isRowValid(row_num):
    return len(set(sudoku_ok[row_num])) == 9


#validate column
def isColValid(col_num):
    col = [item[col_num] for item in sudoku_ok]
    return len(set(col)) == 9


#validate cell
def isCelValid(cel_row, cel_col):
    vals = sudoku_ok[cel_row][cel_col:cel_col + 3]
    vals.extend(sudoku_ok[cel_row + 1][cel_col:cel_col + 3])
    vals.extend(sudoku_ok[cel_row + 2][cel_col:cel_col + 3])
    return len(set(vals)) == 9


#validate sudoku
def validateSudoku():
    for i in range(0, 9):
        if not isRowValid(i):
            return False
        if not isColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isCelValid(i, j):
                return False
    return True


if validateSudoku():
    print("Sudoku is valid.")
else:
    print("Sudoku is not valid.")

validateSudoku()
