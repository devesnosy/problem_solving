# https://codeforces.com/problemset/problem/136/A

n = int(input())

result = [0] * n
pis = [int(s) for s in input().split()]

for i in range(n):
    pi = pis[i]
    result[pi - 1] = i + 1

print(*result)
