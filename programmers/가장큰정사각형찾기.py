def solution(board):
    m, n = len(board), len(board[0])

    c_board = [[0]*n for i in range(m)]
    c_board[0] = board[0]
    for i in range(1, m):
        c_board[i][0] = board[i][0]

    for i in range(m):
        for j in range(1, n):
            if board[i][j] == 1:
                c_board[i][j] = min(c_board[i-1][j-1], c_board[i-1][j], c_board[i][j-1]) + 1
    
    c_max = max([max(list(i)) for i in c_board])

    return c_max**2