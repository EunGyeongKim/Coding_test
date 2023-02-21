import numpy as np

def solution(board):
    tmp = np.pad(board, ((1,1), (1,1)), constant_values = -1)
    boom = np.pad(board, ((1,1), (1,1)), constant_values = -1)

    n = len(board)
    for i in range(1,n+1):
        for j in range(1, n+1):
            if tmp[i][j] > 0:
                for i1 in range(i-1, i+2):
                    for j1 in range(j-1, j+2):
                        boom[i1][j1] = 1

    boom = np.delete(boom, 0, axis =1)
    boom = np.delete(boom, -1, axis =1)
    boom = np.delete(boom, 0, axis =0)
    boom = np.delete(boom, -1, axis =0).tolist()
    
    a = 0
    for i in boom:
        a += i.count(0)

    return a
