# https://codeforces.com/problemset/problem/116/A

n = int(input())

np = 0
npm = np
for _ in range(n):
    a, b = map(int, input().split())
    np -= a
    np += b
    npm = max(np, npm)

print(npm)
