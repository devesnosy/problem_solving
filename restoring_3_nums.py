# https://codeforces.com/problemset/problem/1154/A

xs = [int(s) for s in input().split()]
abc = max(xs)

print(*((abc - x) for x in xs if x != abc))
