import numpy as np

array5 = np.full((10,15),5)
for index_i, i in enumerate(array5):
    for index_j, j in enumerate(i):
        if index_i % 2 == 0:
            if index_j % 2 == 0:
                array5[index_i][index_j]+=3
            else:
                pass
        else:
            if index_j % 2 == 0:
                array5[index_i][index_j]-=5
            else:
                array5[index_i][index_j]+=3
print(array5)
