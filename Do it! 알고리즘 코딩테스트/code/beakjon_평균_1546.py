n = input()
n_list = list(map(int, input().split()))
list_max = max(n_list)
list_sum = sum(n_list)

print(float(list_sum) * 100 / float(list_max) / float(n))