import numpy as np
import pandas as pd

grid = np.random.randint(1, 9, (9, 9))

grid2 = [[9, 2, 3, 4, 5, 6, 7, 8, 1], [7, 2, 3, 4, 5, 6, 7, 8, 9],
         [9, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 2, 6, 7, 8, 9],
         [5, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 3, 6, 7, 8, 9],
         [5, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [5, 2, 3, 4, 1, 6, 7, 8, 9]]

def grid_checker():
    for r in grid:
        if sum(r) == 45:
            order = sorted(r)
            order_string = ''.join(map(str, order))
            print(str(r) + str(order_string))
            if order_string == '123456789':
                print("cette ligne est correct")
        else:
            print(str(r) + "Ligne fausse.Il y a des chiffres qui se repete")

grid_checker()
