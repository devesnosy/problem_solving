# https://codeforces.com/problemset/problem/1352/A

t = int(input())

for _ in range(t):
    n = input()[::-1]
    i = 0
    # Skip leading zeros
    while i < len(n) and n[i] == "0":
        i += 1

    print(sum(c != "0" for c in n[i:]))
    print(*(n[j] + "0" * j for j in range(i, len(n)) if n[j] != "0" ))
