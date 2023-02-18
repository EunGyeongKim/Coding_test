# import sys
# input = sys.stdin.readline

a = int(input())

start = 1
count = 1
end = 1
sum = 1

while end != a:
    if sum == a:
        count += 1
        end += 1
        sum += end
    elif sum > a:
        sum -= start
        start += 1
    else :
        end += 1
        sum += end
        

print(count)