import numpy as np

grid = np.random.randint(1, 9, (9, 9))

grid_ok = [[8, 3, 5, 4, 1, 6, 9, 2, 7], [2, 9, 6, 8, 5, 7, 4, 3, 1],
           [4, 1, 7, 2, 9, 3, 6, 5, 8], [5, 6, 9, 1, 3, 4, 7, 8, 2],
           [1, 2, 3, 6, 7, 8, 5, 4, 9], [7, 4, 8, 5, 2, 9, 1, 6, 3],
           [6, 5, 2, 7, 8, 1, 3, 9, 4], [9, 8, 1, 3, 4, 5, 2, 7, 6],
           [3, 7, 4, 9, 6, 2, 8, 1, 5]]


def check_row():
    for r in grid:
        order = sorted(r)
        order_string = ''.join(map(str, order))
        print(str(r) + str(order_string))
        if not order_string == '123456789':
            print(False)
        else:
            print(True)


def check_column():
    column = grid.transpose()
    for c in column:
        order_col = sorted(c)
        order_col_str = ''.join(map(str, order_col))
        if not order_col_str == '123456789':
            print(False)
        else:
            print(True)


check_column()
