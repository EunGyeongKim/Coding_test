
def solution(n, s):
    answer = []

    if s//n <= 0:
        return [-1]

    if s%n == 0:
        for i in range(n):
            answer.append(int(s/n))
    else:
        answer = [s//n for _ in range(n)]
        for i in range(s%n):
            answer[i] += 1

    return sorted(answer)