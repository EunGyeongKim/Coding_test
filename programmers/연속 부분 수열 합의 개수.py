def solution(elements):
    answer = 0
    # 1개 
    tmp = list(set(elements))

    len_e = len(elements)

    for i in range(2, len_e):
        for j in range(len_e):
            if (j+i) <= len_e:
                num = elements[j:j+i]
                tmp.append(sum(num))
            else:
                t_n = i-len(elements[j:])
                num = elements[j:] + elements[:t_n]
                tmp.append(sum(num))
    tmp.append(sum(elements))
    
    return len(list(set(tmp)))

