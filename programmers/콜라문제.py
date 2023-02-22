def solution(a, b, n):
    answer = 0
    while n >= a:
        # print(a, n, answer)
        a1, a2 = divmod(n, a)
        answer += a1*b
        n = a2 + a1*b

    return answer
    