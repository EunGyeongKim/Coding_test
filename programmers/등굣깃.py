
def solution(m, n, puddles):
    map = [[1]*(m+1) for i in range(n+1)]
    map[0] = [0] * (m+1)
    for i in range(n+1):
        map[i][0] = 0
    puddles = [[q,p] for [p,q] in puddles]      

    for i in puddles:
        map[i[0]][i[1]] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j==1:
                continue
            if [i, j] in puddles:
                map[n][m] = 0
            else:
                map[i][j] = ( map[i-1][j]+map[i][j-1] ) % 1000000007 

    return map[n][m]
