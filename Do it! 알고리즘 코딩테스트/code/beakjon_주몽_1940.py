# import sys
# input = sys.stdin.readline
n = int(input())
m = int(input())
mlist = sorted(list(map(int, input().split())))

start = 0
end = n-1
count = 0

while start <= end:

    if m == (mlist[start]+mlist[end]):
        start += 1
        end -= 1
        count += 1
    elif m < (mlist[start]+mlist[end]):
        end -=1
    else:
        start += 1

print(count)