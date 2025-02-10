# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())

dragons = [[int(s) for s in input().split()] for _ in range(n)]

dragons.sort(key=lambda d: d[0])

for x, y in dragons:
    if s <= x:
        print("NO")
        exit()
    s += y

print("YES")
