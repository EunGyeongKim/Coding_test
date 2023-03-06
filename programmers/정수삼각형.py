def solution(triangle):
    tmp = [[0 for j in i] for i in triangle]
    tmp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if i == 1:
                tmp[i][j] = tmp[0][0] + triangle [i][j]
            elif j == 0:
                tmp[i][j] = tmp[i-1][j] + triangle [i][j]
            elif j == (len(triangle[i])-1):
                tmp[i][j] = tmp[i-1][j-1]+ triangle [i][j]
            else:
                tmp[i][j] = max(tmp[i-1][j], tmp[i-1][j-1])+ triangle [i][j]
            # print(i,j, end=' ')
        # print('\n')
    # print(tmp)
    answer = 0

    return max(tmp[len(triangle)-1])