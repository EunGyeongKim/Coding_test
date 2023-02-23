def solution(a):
    tmp = ''
    for i in range(1, len(a)):
        tmp += str(i) * (a[i]//2)

    tmp = tmp + '0' + tmp[::-1]

    return tmp