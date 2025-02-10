# https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())

fs = [int(s) for s in input().split()]

fs.sort()

ws = 0
min_diff = fs[ws + n - 1] - fs[ws]
ws = 1
while (ws + n - 1) < m:
    min_diff = min(min_diff, fs[ws + n - 1] - fs[ws])
    ws += 1

print(min_diff)
