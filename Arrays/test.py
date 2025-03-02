# Defining number of rows and columns in matrix
rows = 3
cols = 3

# Declaring a matrix of size 3 X 3, and
# initializing it with value zero

arr = [[0]*cols]*rows

arr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


"""
      column
 row [1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]
"""


def sort_matrix_column_wise(mtx):

    sort_mtx = []

    for col in list(zip(*mtx)):
        sort_mtx.append(sorted(col))

    return list(map(list, zip(*sort_mtx)))

def sort_matrix_row_wise(mtx):

    sorted_mtx = []

    for row in mtx:
        sorted_mtx.append(sorted(row))

    return sorted_mtx


mat =[  [1, 6, 10 ],
        [ 8, 5, 9 ],
        [ 9, 4, 15 ],
        [ 7, 3, 60 ] ]

print('Column sort')
print(sort_matrix_column_wise(mat))
print('\nRow sort')
print(sort_matrix_row_wise(mat))