import sys
input = sys.stdin.readline

a, b = map(int, input().split())
table=[[0]*(a+1)]
prefix=[[0]*(a+1) for _ in range(a+1)]

for i in range(a):
    row = [0] + [int(x) for x in input().split()]
    table.append(row)

for i in range(1, a+1):
    for j in range(1, a+1):
        prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1] - 
                        prefix[i-1][j-1] + table[i][j] )
        
# print(prefix)
for i in range(b):
    x1, y1, x2, y2 = map(int, input().split())
    answer = (prefix[x2][y2] + prefix[x1-1][y1-1] 
              - prefix[x2][y1-1] - prefix[x1-1][y2])
    print(answer)