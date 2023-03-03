def solution(n):

    tlist = [4,1,2,4]

    base = 3

    result = ''
    while n:
        result=str(tlist[n%base])+result
        n=int(n//3.0000000001)
        # print(i, result )

    return result