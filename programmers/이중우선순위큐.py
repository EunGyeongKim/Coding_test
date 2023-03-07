from collections import deque

def solution(operations):
    answer = []

    for i in operations:
        tmp = i.split()
        # print(tmp[0], tmp[1])
        if tmp[0] == 'I':
            answer.append(int(tmp[1]))
        elif tmp[0] == 'D':
            if len(answer) == 0:
                continue
            else:
                if tmp[1] == '1':
                    answer.remove(max(answer))
                else :
                    answer.remove(min(answer))
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]