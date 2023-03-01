from collections import deque
def solution(k, tangerine):
    size = [0] * (max(tangerine)+1)
    answer = 0
    count = 0

    for i in tangerine:
        size[i] += 1

    size = sorted(size, reverse=True)
    s = deque(size)

    while count < k:
        count += s.popleft()
        answer += 1

    return answer