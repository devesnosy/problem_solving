# https://codeforces.com/problemset/problem/1328/A

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    aob, amb = divmod(a, b)
    if amb == 0:
        print("0")
    else:
        print((aob + 1) * b - a)
