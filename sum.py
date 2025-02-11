# https://codeforces.com/problemset/problem/1742/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a == (b+c)) or (b == (a + c)) or (c == (a + b)):
        print("YES")
    else:
        print("NO")
