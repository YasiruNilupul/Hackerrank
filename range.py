from itertools import product

n, m = map(int, input().split())
lists = []
for i in range(n):
    lst = list(map(int, input().split()))[1:]
    lists.append(lst)

max_sum = 0
for values in product(*lists):
    s = sum(v**2 for v in values) % m
    max_sum = max(max_sum, s)

print(max_sum)
