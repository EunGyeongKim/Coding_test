import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n :
        return 0
    else: 
        works = [-i for i in works]
        heapq.heapify(works)
        # print(works)

        for i in range(n):
            tmp = heapq.heappop(works)
            heapq.heappush(works, tmp+1)
    
    for i in works:
        answer += i**2
    return answer
