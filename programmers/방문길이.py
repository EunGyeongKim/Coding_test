def solution(dirs):
    x, y = 0, 0
    o_x, o_y = 0,0
    check = []
    answer = -1
    
    for i in dirs:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'R':
            x += 1
        elif i == 'L':
            x -= 1
        if x > 5:
            x = 5
        elif x < -5:
            x = -5
        elif y >5:
            y = 5
        elif y < -5:
            y = -5
            
        if [o_x, o_y, x, y] not in check and [o_x, o_y] != [x, y] and [x, y, o_x, o_y] not in check:
            check.append([o_x, o_y, x, y])
        
        o_x, o_y = x, y

    return len(check)