import numpy as np

grid = np.random.randint(1, 9, (9, 9))

grid_ok = [[8, 3, 5, 4, 1, 6, 9, 2, 7], [2, 9, 6, 8, 5, 7, 4, 3, 1],
           [4, 1, 7, 2, 9, 3, 6, 5, 8], [5, 6, 9, 1, 3, 4, 7, 8, 2],
           [1, 2, 3, 6, 7, 8, 5, 4, 9], [7, 4, 8, 5, 2, 9, 1, 6, 3],
           [6, 5, 2, 7, 8, 1, 3, 9, 4], [9, 8, 1, 3, 4, 5, 2, 7, 6],
           [3, 7, 4, 9, 6, 2, 8, 1, 5]]


def check_row():
    for r in grid_ok:
        order = sorted(r)
        order_string = ''.join(map(str, order))
        print(str(r) + str(order_string))
        if order_string == '123456789':
            print("cette ligne est correct")
    else:
        print(str(r) + "Il y a des chiffres qui se repete")


def check_column():
    print(grid)
    column = grid.transpose()
    for c in column:
        if sum(c) == 45:
            order_col = sorted(c)
            order_col_str = ''.join(map(str, order_col))
            print(str(c) + str(order_col_str)+" ligne fausse")
            if order_col_str == '123456789':
                print("cette colonne est correct")
                return True
    else:
        print(str(c) + "Colonne fausse.Il y a des chiffres qui se repete")




check_row()
