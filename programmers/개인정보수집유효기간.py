
def solution(today, terms, privacies):
    term = {}
    t_day = list(map(int, today.split('.')))
    answer = []
    today = t_day[0]*28*12 + t_day[1]*28 + t_day[2]
    # 약관
    for i in terms:
        tmp = i.split()
        term[tmp[0]] = tmp[1]


    for a, i in enumerate(privacies):
        s_day = i.split()
        term_month = int(term[s_day[1]])
        end_day = list(map(int,s_day[0].split('.')))
        
        dead = end_day[0]*28*12 + end_day[1]*28 + end_day[2] + term_month*28 -1

        if today > dead:
            answer.append(a+1)

    return answer
