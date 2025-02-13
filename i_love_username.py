# https://codeforces.com/problemset/problem/155/A

n = int(input())
p_iter = map(int, input().split())

running_max = next(p_iter)
running_min = running_max
n_amazing = 0
for p in p_iter:
    if p > running_max:
        running_max = p
        n_amazing += 1
    elif p < running_min:
        running_min = p
        n_amazing += 1

print(n_amazing)
