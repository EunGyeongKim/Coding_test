import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = False
arrive = False
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v, d):
    global arrive
    if d == 5:
        arrive=True
        return 
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            dfs(i, d+1)
    visited[v] = False

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive :
    print(1)
else: 
    print(0)
