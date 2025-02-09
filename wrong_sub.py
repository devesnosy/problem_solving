# https://codeforces.com/problemset/problem/977/A

n, k = map(int, input().split())

for _ in range(k):
    no10, nm10 = divmod(n, 10)
    if nm10 == 0:
        n = no10
    else:
        n -= 1

print(n)
