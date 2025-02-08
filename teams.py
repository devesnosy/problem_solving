# https://codeforces.com/contest/231/problem/A

n = int(input())

nsol = 0
for _ in range(n):
    nsure = sum(map(int, input().split()))
    if nsure >= 2:
        nsol += 1

print(nsol)
