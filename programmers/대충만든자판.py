def solution(a, b):
    tmp = []
    min_alpha = {}

    for i in a:
        for a, j in enumerate(i):
            if j not in tmp:
                tmp.append(j)
                min_alpha[j] = a+1
            else:
                min_alpha[j] = min(min_alpha[j], a+1)

    answer = []
    for i in b:
        count = 0
        for j in i:
            if j in min_alpha:
                count += min_alpha[j] 
            else:
                count = -1
                break
        if count != 0:
            answer.append(count)
        else:
            answer.append(-1)


    return answer
    