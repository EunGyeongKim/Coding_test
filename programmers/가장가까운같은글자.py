def solution(a):
    a = list(a)
    tmp = []
    answer = []

    for i in a:
        # first word
        if i not in answer:
            answer.append(i)
            tmp.append(-1)
        # already exist
        else:
            print(answer, tmp)
            location = len(answer) - (len(answer) - answer[::-1].index(i))+1
            answer.append(i)
            tmp.append(location)

    return tmp