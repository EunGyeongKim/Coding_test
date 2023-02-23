def solution(numbers, hand):
    #왼쪽, 오른쪽이 누를수 있는 번호
    left_list = ['1', '4', '7', '*']
    right_list = ['3', '6', '9', '#']

    #위치
    left, right = '*', '#'

    #위치체크
    check = ['2', '5', '8', '0']
    answer = ''

    for i in numbers:
        i = str(i)
        if i in left_list:
            left = i
            tmp ='L'
        elif i in right_list:
            right = i
            tmp ='R'
        
        if i in ['2', '5', '8', '0']:
            c_index = check.index(i)
            if left in left_list:
                l_diff = abs(left_list.index(left) - c_index)+1
                if right in right_list :
                    r_diff = abs(right_list.index(right) - c_index)+1
                else :
                    r_diff = abs(check.index(right) - c_index)
            else:
                l_diff = abs(check.index(left) - c_index)
                if right in right_list :
                    r_diff = abs(right_list.index(right) - c_index)+1
                else :
                    r_diff = abs(check.index(right) - c_index)

            if l_diff < r_diff:
                left = i
                tmp ='L'
            elif l_diff > r_diff:
                right = i
                tmp ='R'
            else:
                if hand == "right": 
                    right = i
                    tmp ='R'
                else: 
                    left = i
                    tmp ='L'
        answer += tmp
    return answer