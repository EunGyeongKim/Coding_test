n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    find = False
    target = i

    start = 0
    end = len(n_list)-1

    while start <= end:
        midi = int((start + end)/2)
        midv = n_list[midi]

        if midv > target:
            end = midi-1
        elif midv < target:
            start = midi+1
        else:
            find = True
            break
    if find :
        print(1)
    else :
        print(0)