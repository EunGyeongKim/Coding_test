def solution(number, limit, power):
    def cal_power(n, limit, power):
        n_power =0
        for i in range(1, int(n**(1/2))+1):
            if n % i== 0:
                if i == n//i:
                    n_power += 1
                else:
                    n_power += 2
            if n_power > limit:
                return power
        return n_power

    answer = 1
    for i in range(2, number+1):
        answer += cal_power(i, limit, power)

    return answer