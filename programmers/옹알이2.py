def solution(b):
    answer = 0
    check_list =["aya", "ye", "woo", "ma"]

    for i in range(len(b)):
        for j in check_list:
            # repeat same word
            if j*2 in b[i]:
                continue
            b[i] = b[i].replace(j, ' ')
    for i in b:
        if len(i.strip()) == 0:
            answer+= 1

    return answer
