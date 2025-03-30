# https://codeforces.com/problemset/problem/581/A

a, b = map(int, input().split())

r1 = min(a, b)
a -= r1
b -= r1

print(r1, max(a, b) // 2)
