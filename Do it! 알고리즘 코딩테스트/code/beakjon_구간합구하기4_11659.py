import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

prefix = [0]
for i in n_list:
    prefix.append((i+prefix[-1]))
# print(prefix)

for i in range(m):
    tmp = list(map(int, input().split()))
    print(prefix[tmp[1]]- prefix[tmp[0]-1])