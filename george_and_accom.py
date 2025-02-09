# https://codeforces.com/problemset/problem/467/A

n = int(input())

answer = 0
for _ in range(n):
    p, q = map(int, input().split())
    if (q - p) >= 2:
        answer += 1

print(answer)
