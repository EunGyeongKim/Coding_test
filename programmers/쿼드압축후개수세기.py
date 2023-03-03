def solution(arr):
    answer = []
    
    def fac(x, y, n):
        tlist = []
        if n == 1:
            return [arr[x][y]]
        else:
            tmp = sum([sum(i[y:y+n]) for i in arr[x:x+n] ])
            if tmp == 0:
                return [0]
            elif tmp == n*n:
                return [1] 
            else:
                return (fac(x, y, n//2) + 
                        fac((x+n//2), y, n//2) + 
                        fac(x, (y+n//2), n//2) + 
                        fac((x+n//2), (y+n//2), n//2))
    tmp =  fac(0, 0, len(arr))
    return [tmp.count(0), tmp.count(1)]