# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())

w = 0
for hp in map(int, input().split()):
    if hp > h:
        w += 2
    else:
        w += 1

print(w)
