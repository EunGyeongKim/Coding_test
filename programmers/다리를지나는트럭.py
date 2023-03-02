from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    tmp = [0]* bridge_length

    truck = deque(truck_weights)
    temp = deque(tmp)
    temp_sum = 0
    
    for i in range(bridge_length * len(truck_weights)+1):
        a = temp.popleft()
        temp_sum -= a
        if temp_sum == 0 and len(truck) ==0:
            break
        if temp_sum == 0:
            a = truck.popleft()
            temp_sum +=a
            temp.append(a)
        else:
            if len(truck) ==0:
                tmp_truck = 0
            else :
                tmp_truck = truck[0]

            if (temp_sum+tmp_truck) > weight:
                temp.append(0)
            else:
                if len(truck) == 0:
                    temp.append(0)
                else:
                    a = truck.popleft()
                    temp_sum +=a
                    temp.append(a)
        # print(i, temp, truck)
    return i+1
