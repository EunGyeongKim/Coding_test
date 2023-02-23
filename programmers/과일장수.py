def solution(a,b,c):
    c = sorted(c, reverse=True)
    score = 0

    for i in range(0, len(c), b):
        if len(c[i:i+b]) == b:
            score += b * min(c[i:i+b])
            # print(b * min(c[i:i+b]), c[i:i+b])
    return score