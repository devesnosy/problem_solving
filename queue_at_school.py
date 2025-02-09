# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())

s = list(input())

for _ in range(t):
    i = 0
    while (i + 1) < n:
        if s[i] == "B" and s[i + 1] == "G":
            s[i] = "G"
            s[i + 1] = "B"
            i += 2
        else:
            i += 1
print("".join(s))
