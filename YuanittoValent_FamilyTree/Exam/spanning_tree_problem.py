from cmath import inf

from numpy import empty


import numpy as np

def min_extension(con, g):
    min_weight = inf
    for i in con:
        for j in range(len(g)):
            if j not in con and 0 < g[i][j] < min_weight:
                v, w = i,j
                min_weight = g[i][j]
    return v, w

def mst(graph):
    tree = np.zeros((len(graph),len(graph)))
    con = [0]
    result = [0]*len(graph)
    result[con[0]] = None
    while len(con) < len(graph):
        i, j = min_extension(con,graph)
        tree[i][j], tree[j][i] = graph[i][j], graph[j][i]
        con += [j]
        result[j] = i   
    return result

graph = np.array([
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,1,1],
    [1,1,1,0,0],
    [0,1,1,0,0],
    ])

print(mst(graph))