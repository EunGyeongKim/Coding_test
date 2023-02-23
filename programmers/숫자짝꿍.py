def solution(x, y):
    xlist = [0]*10
    ylist = [0]*10
    result = ''

    for i in x:
        xlist[int(i)] += 1
    for i in y:
        ylist[int(i)] += 1
    
    for i in range(9, -1, -1):
        tmp_min = min(xlist[i], ylist[i])
        if i == 0 and tmp_min != 0 and result == '' :
            return '0'
        result = ''.join([result, str(i)*tmp_min])

    if len(result) == 0:
        return '-1'
    else:
        return result
