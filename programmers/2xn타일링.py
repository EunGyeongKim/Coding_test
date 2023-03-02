def solution(n):
    memory = [0]*60000
    memory[0] = 1
    memory[1] = 2

    for i in range(1, n+1):
        memory[i] = (memory[i-1] + memory[i-2])%1000000007

    return memory[n]