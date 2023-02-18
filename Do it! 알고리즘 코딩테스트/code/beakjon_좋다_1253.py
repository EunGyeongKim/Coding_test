# import sys
# input = sys.stdin.readline

n = int(input())
m = sorted(list(map(int,input().split())))

count = 0

for i in range(n):
    start = 0
    end = n-1
    while start < end:
        tmp = m[start] + m[end]
        if tmp == m[i]:
            if start != i and end != i:
                count+= 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif tmp < m[i]:
            start += 1
        else :
            end -= 1


print(count)