import math
def solution(n):
    answer = []
    for i in n:
        tmp = bin(i)[2:].zfill(len(bin(i)[2:])+1)
        tmp = (tmp[::-1])
        for j in range(len(tmp)):
            if tmp[j] == '0':
                if j ==0 :
                    i += 1
                else:
                    # print(i, j, bin(i)[2:])
                    i += math.pow(2,j-1)
                break
        answer.append(int(i))
            
    return answer