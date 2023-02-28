import string
def solution(n, t, m, p):
    number = ''
    answer = ''

    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]

    for i in range(0, t*m+1):
        number += (convert(i, n))
    
    if p == m:
        p = 0

    for a, i in enumerate(number):
        if (a+1) % m == p:
            answer += i
            t -=1
        if t == 0:
            break

    return answer.upper()