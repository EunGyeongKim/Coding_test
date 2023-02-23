from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)

    comp1 , comp2 = c1.popleft(), c2.popleft()
    for i in goal:
        if comp1 == i:
            if len(c1)>0:
                comp1 = c1.popleft()
        elif comp2 == i :
            if len(c2)>0:
                comp2 = c2.popleft()
        else:
            return 'No'

    return "Yes"