def solution(k, score):
    answer = []
    rank = []

    for i in score:
        if len(rank) == 0:
            rank.append(i)
        else:
            if len(rank) < k:
                rank.append(int(i))
            elif min(rank) < i:
                rank[rank.index(min(rank))] = i

        answer.append(min(rank))

        # rank = sorted(rank)
        # print(min(rank), i, rank, )

    return answer