def solution(prices):
    answer = []


    for i in range(len(prices)):
        count = 0
        for j in range(i+1,len(prices)):
            # print(i, j, prices[i], prices[j])
            count += 1
            if prices[i] > prices[j]:
                break
        # print('append :', count)
        answer.append(count) 

    return answer