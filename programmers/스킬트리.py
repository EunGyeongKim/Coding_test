def solution(skill, skill_trees):
    answer = 0
    s_list =[]
    s = ''

    for i in skill:
        s += i
        s_list.append(s)

    for i in skill_trees:
        for j in i:
            if j not in skill:
                i = i.replace(j, '')
                
        if i in s_list or i == '':
            answer += 1

    return answer