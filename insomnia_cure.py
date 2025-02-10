# https://codeforces.com/problemset/problem/148/A

k, l, m, n, d = (int(input()) for _ in range(5))

answer = 0
for i in range(1, d + 1):
    if 0 in (i % k, i % l, i % m, i % n):
        answer += 1

print(answer)
