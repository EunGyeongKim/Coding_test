import numpy as np
def solution(m, n, board):
    answer = 0

    # 테두리에 0 padding 추가
    n_board = np.array([[j for j in i] for i in board])
    n_board = np.pad(n_board, pad_width=((1, 0), (1, 0)), mode='constant', constant_values = 0)

    def check4(board):
        tlist = []
        # 4개 붙어있을 경우 tlist append
        for i in range(1, m+1):
            for j in range(1, n+1):
                tmp = n_board[i][j]
                if tmp == n_board[i-1][j-1] and tmp == n_board[i][j-1] and tmp == n_board[i-1][j] and tmp != '0':
                    if [i, j] not in tlist:
                        tlist.append([i, j])
                    if [i-1, j] not in tlist:
                        tlist.append([i-1, j])
                    if [i, j-1] not in tlist:
                        tlist.append([i, j-1])
                    if [i-1, j-1] not in tlist:
                        tlist.append([i-1, j-1])
        return tlist

    def reform_borad(board):
        for j in range(1, n+1):
            for i in range(m, 0, -1):
                # print(board)
                # print(i, j, board[i][j])
                if board[i][j] == '0' and board[i-1][j] != '0':
                    for k in range(i, m+1):
                        if board[k][j] == '0' and board[k-1][j] != '0':
                            board[k][j], board[k-1][j] =  board[k-1][j], board[k][j] 
                    
        return board
    
    checklist = []
    
    checklist = check4(n_board)

    while checklist:
        answer += len(checklist)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if [i,j] in checklist:
                    n_board[i][j] = '0'
        
        reform_borad(n_board)
        checklist = check4(n_board)
        
    return answer